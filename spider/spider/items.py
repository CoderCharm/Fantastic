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

class FanChannelItem(scrapy.Item):
    """文章来源库"""
  
    channel_id = scrapy.Field()  # 主键ID
    channel_name = scrapy.Field()  # 平台名称
    channel_status = scrapy.Field()  # 开启状态 默认开启


class FanTaskCateItem(scrapy.Item):
    """文章分类表"""

    cate_id = scrapy.Field()
    cate_name = scrapy.Field() # 分类名
    cate_status = scrapy.Field()  # 开启状态 默认开启

  


class FanItem(scrapy.Item):
    """文章列表"""
    t_author = scrapy.Field() # 原文作者
    t_author_img = scrapy.Field()  # 作者头像链接
    t_title = scrapy.Field()  # 不允许为空
    t_desc = scrapy.Field()  # 简介 不允许为空
    t_image = scrapy.Field()  # 简介 不允许为空
    t_url = scrapy.Field()  # 原文链接 先去掉
    total_click_count = scrapy.Field() # 总点击数
    current_click_count = scrapy.Field() # 当前点击数每天的点击量
    status = scrapy.Field() # 任务状态(0关闭1开启2待审核-1已删除)
    memo = scrapy.Field() # 备注
    t_key = scrapy.Field() # 唯一key 抓取文章源key
    t_read_count = scrapy.Field()  # 文章阅读数
    t_time = scrapy.Field() # 文章发布时间
    p_time = scrapy.Field()  # 推送时间
    article_type = scrapy.Field() # 1：普通类型 2：视频类型
    is_get = scrapy.Field()  # 是否已推送
    is_hot = scrapy.Field() # 是否是热点
    video_second = scrapy.Field()  # 播放时长 秒
    video_url = scrapy.Field() # 视频地址
    tags = scrapy.Field()  # 文章标签
    task_platform = scrapy.Field()  # 文章来源
    grad_read_count = scrapy.Field()  # 抓取阅读数
    grad_forward_count = scrapy.Field()  # 抓取转发数
    grad_comments_count = scrapy.Field()  # 抓取评论数


class FanTaskDetailItem(scrapy.Item):
    """文章详情表"""
    task_id = scrapy.Field()   # 文章id
    task_content = scrapy.Field()  # 文章内容
    task_comment = scrapy.Field()  # 文章评论区预留


