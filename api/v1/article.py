# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:51
# @Desc: 
"""

"""
import time
from flask import request
from flask_restful import Resource

from models import FanTask


class ArticleResource(Resource):
    """Single object resource
    """

    def get(self, item_id):
        return {"ArticleList": 1}
        # print(user_id)

    def post(self, item_id):
        return {"ArticleResource_post": item_id}


class ArticleList(Resource):
    """
    查询文章列表
    """

    def get(self):
        # 实现分页查询的功能 page 页数 size 一页显示的数据 cate 分类查询
        page = request.args.get('page', 1, type=int)
        size = request.args.get('size', 20, type=int)
        cate = request.args.get('cate', '', type=int)
        pages = (int(page) - 1) * 10
        # 判断是否有分类
        if cate:
            info_res = FanTask.query.filter(FanTask.t_cate == cate).order_by(FanTask.task_id.desc()).offset(
                pages).limit(
                size)
        else:
            info_res = FanTask.query.order_by(FanTask.task_id.desc()).offset(pages).limit(size)
        data_list = []
        for info in info_res:
            tmp = {"account": {
                "avatar": info.t_author_img,
                "id": 89, "nickname": info.t_author, "qrcode": None},
                "author": info.t_author,
                'author_id': info.t_author_id,
                "content_url": info.t_url,
                "copyright_stat": 11,
                "cover": info.t_image,
                "digest": info.t_desc,
                "id": 10723,
                "md5_url": info.uuid,
                "published_at": time.strftime("%Y-%m-%d", time.localtime(int(info.create_time[:-3]))),
                "title": info.t_title,
                "top": 0
            }
            data_list.append(tmp)

        data = {
            "code": 200,
            "data": data_list,
            "cate": cate,
            "msg": "success",
            "page": page,
            "size": size,
        }

        return data

    def post(self):
        return {"ArticleList": "post"}
