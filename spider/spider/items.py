# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FanTaskItem(scrapy.Item):
    """文章列表"""
    t_author = scrapy.Field()  # 原文作者
    t_author_img = scrapy.Field()  # 作者头像链接
    t_title = scrapy.Field()  # 不允许为空
    t_desc = scrapy.Field()  # 简介 允许为空
    t_image = scrapy.Field()  # 简介 不允许为空
    t_url = scrapy.Field()  # 原文链接 先去掉
    t_key = scrapy.Field()  # 唯一key 抓取文章源key
    t_read_count = scrapy.Field()  # 文章阅读数
    article_type = scrapy.Field()  # 1：普通类型 2：视频类型
    video_second = scrapy.Field()  # 播放时长 毫秒
    video_url = scrapy.Field()  # 视频地址
    tags = scrapy.Field()  # 文章标签
    task_platform = scrapy.Field()  # 文章来源
    grad_read_count = scrapy.Field()  # 抓取阅读数
    grad_forward_count = scrapy.Field()  # 抓取转发数
    grad_comments_count = scrapy.Field()  # 抓取评论数
    task_content = scrapy.Field()  # 文章内容
