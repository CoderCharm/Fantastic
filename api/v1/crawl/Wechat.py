#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 18:39
# @Author  : wgPython
# @File    : Wechat.py
# @Software: PyCharm
# @Desc    :
"""
微信爬虫手动抓取
"""
import re
import random
import requests_html

from flask import request

from config import UA_WEB_LIST
from extensions import Resource, swagger


class WeChat(Resource):
    """抓取微信文章"""

    def __init__(self):
        self.session = requests_html.HTMLSession()

    def post(self):
        url = request.json.get("url")

        response = self.session.get(url,
                                    headers={
                                        "Host": "mp.weixin.qq.com",
                                        "User-Agent": random.choice(UA_WEB_LIST)
                                    },
                                    verify=False,
                                    )

    @staticmethod
    def replace_img_content(content):
        """
        用来替换其中图片和过滤其他字符
        :param content:
        :return:
        """
        if not content:
            return None
        content = re.sub(r"<(?!/?\s?p|/?\s?img|/?\s?iframe)[^<>]*>", "", content)
        content = re.sub(r"<p[\S\s]*?>", "<p>", content)
        content = re.sub(r"\n", "", content)
        content = re.sub(r"\r", "", content)
        content = re.sub(r"\t", "", content)

        content = re.sub(r"<script[\s\S]*?>[\s\S]*?</script>", "", content)

        # 替换里面的视频
        content = re.sub(
            r"<iframe[\S\s]*?data-src=[\"\'](?P<base>http.*?\?).*?(?P<vid>vid=\w+).*?[\"\'][\s\S]*?</iframe>",
            "<iframe class=\"ql-video addVideo\" style=\"width:100%; min-height:200px\" src=\"\g<base>\g<vid>\"></iframe>",
            content)
        # 替换里面的图片
        content = re.sub(r"<img[\s\S]*?data-src=[\'\"]http[s]?:.*?(cn|com)(?P<s2>.*?)[\"\'][\s\S]*?>",
                         "<img src=\"http://images.xiaocao01.cn\g<s2>\" >", content)

        word_number = re.findall(r"[\u4e00-\u9fa5]+", content)
        video_number = re.findall(r"<iframe[\s\S]*?iframe>", content)

        # 判断文章类型 字数少于30 视频数量大于等于 1个
        if len(word_number) <= 30 and len(video_number) >= 1:
            # 视频
            article_type = "1"
        else:
            # 文章
            article_type = "2"

        return content, article_type
