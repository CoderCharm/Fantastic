#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 10:12
# @Author  : wgPython
# @File    : article.py
# @Software: PyCharm
# @Desc    :
"""
文章模型类
"""
import time

from extensions import db
from api.models.index import BaseModel


class FanChannel(db.Model, BaseModel):
    """
    文章来源库
    """
    channel_id = db.Column(db.Integer)  # 主键ID
    channel_name = db.Column(db.String(50), comment="平台名称")  # 平台名称
    channel_status = db.Column(db.Boolean, default=True, comment="平台开启状态")  # 开启状态 默认开启

    def __init__(self, **kwargs):
        super(FanChannel, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Channel: {self.channel_name}>"


class FanTaskCate(db.Model, BaseModel):
    """
    文章分类表
    """
    cate_id = db.Column(db.Integer)
    cate_name = db.Column(db.String(16), nullable=False, comment="分类名")  # 分类名
    cate_status = db.Column(db.Boolean, default=True, comment="开启状态")  # 开启状态 默认开启

    def __init__(self, **kwargs):
        super(FanTaskCate, self).__init__(**kwargs)

    def __repr__(self):
        return f"<TaskCate: {self.cate_name}>"


class FanTask(db.Model, BaseModel):
    """
    文章列表
    """
    task_id = db.Column(db.String(64), unique=True, comment="文章id")
    t_author_id = db.Column(db.String(64), comment="作者id")  # 作者id
    t_title = db.Column(db.String(256), nullable=False, comment="标题")  # 不允许为空
    t_desc = db.Column(db.String(512), comment="简介")  # 简介 不允许为空
    t_image = db.Column(db.String(1024), comment="封面图")  # 封面图
    t_url = db.Column(db.String(1024), comment="原文链接")  # 原文链接 先去掉
    t_cate = db.Column(db.String(8), comment="分类id")  # 添加分类id 和 分类表关联
    total_click_count = db.Column(db.Integer, comment="总点击数")  # 总点击数
    current_click_count = db.Column(db.Integer, comment="每天点击数")  # 当前点击数每天的点击量
    status = db.Column(db.SmallInteger, default="0", comment="任务状态")  # 任务状态(0关闭1开启2待审核-1已删除)
    memo = db.Column(db.VARCHAR(128), comment="备注")  # 备注
    t_key = db.Column(db.VARCHAR(164), unique=True, comment="文章唯一id")  # 唯一key 抓取文章源key
    t_time = db.Column(db.String(64), default=int(time.time() * 1000), comment="文章发布时间")  # 文章发布时间
    p_time = db.Column(db.String(64), default=int(time.time() * 1000), comment="文章推送时间")  # 推送时间
    article_type = db.Column(db.Integer, nullable=False, comment="文章类型")  # 1：普通类型 2：视频类型
    is_get = db.Column(db.Boolean, default=False, comment="是否已推送")  # 是否已推送
    is_hot = db.Column(db.Boolean, default=False, comment="是否是热点")  # 是否是热点
    video_second = db.Column(db.SmallInteger, comment="播放时长(毫秒)")  # 播放时长 毫秒
    video_url = db.Column(db.VARCHAR(255), comment="视频地址")  # 视频地址
    tags = db.Column(db.String(1024), comment="文章标签")  # 文章标签
    task_platform = db.Column(db.SmallInteger, comment="文章涞源")  # 文章来源
    grad_read_count = db.Column(db.SmallInteger, comment="抓取来源阅读数")  # 抓取阅读数
    grad_forward_count = db.Column(db.SmallInteger, comment="抓取来源转发数")  # 抓取转发数
    grad_comments_count = db.Column(db.SmallInteger, comment="抓取涞源评论数")  # 抓取评论数

    def __init__(self, **kwargs):
        super(FanTask, self).__init__(**kwargs)

    def __repr__(self):
        return f"<FanTask: {self.t_title}>"


class FanTaskDetail(db.Model, BaseModel):
    """
    文章详情表
    """
    task_id = db.Column(db.Integer, nullable=False, primary_key=True)  # 文章id
    task_content = db.Column(db.Text, nullable=False)  # 文章内容
    task_comment = db.Column(db.Text)  # 文章评论区预留

    def __init__(self, **kwargs):
        super(FanTaskDetail, self).__init__(**kwargs)


class FanTaskAuthor(db.Model, BaseModel):
    """
    作者表
    """
    t_author_id = db.Column(db.String(64))  # 作者id
    t_author = db.Column(db.String(256), comment="作者名称")  # 原文作者
    t_author_img = db.Column(db.String(1024), comment="作者头像链接")  # 作者头像链接
    channel_id = db.Column(db.Integer, comment="来源平台")  # 作者来源id

    def __init__(self, **kwargs):
        super(FanTaskAuthor, self).__init__(**kwargs)

