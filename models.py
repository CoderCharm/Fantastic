# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 15:11
# @Desc: 
"""
ORM创建数据库
不使用外键关系
"""
import time

from extensions import db


class BaseModel(object):
    """
    模型基类，为每个模型补充创建时间与更新时间
    """
    create_time = db.Column(db.String(64), index=True, default=int(time.time() * 1000))  # index给定索引
    update_time = db.Column(db.String(64), default=int(time.time() * 1000))  # 记录的更新时间


class FanChannel(BaseModel, db.Model):
    """
    文章来源库
    """
    channel_id = db.Column(db.Integer, primary_key=True)  # 主键ID
    channel_name = db.Column(db.String(50))  # 平台名称
    channel_status = db.Column(db.Boolean, default=True)  # 开启状态 默认开启

    def __init__(self, **kwargs):
        super(FanChannel, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Channel: {self.channel_name}>"


class FanTaskCate(BaseModel, db.Model):
    """
    文章分类表
    """
    cate_id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(16), nullable=False)  # 分类名
    cate_status = db.Column(db.Boolean, default=True)  # 开启状态 默认开启

    def __init__(self, **kwargs):
        super(FanTaskCate, self).__init__(**kwargs)

    def __repr__(self):
        return f"<TaskCate: {self.cate_name}>"


class FanTask(BaseModel, db.Model):
    """
    文章列表
    """
    task_id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(64), unique=True)
    t_author = db.Column(db.String(256))  # 原文作者
    t_author_id = db.Column(db.String(64))  # 作者id
    t_author_img = db.Column(db.String(1024))  # 作者头像链接
    t_title = db.Column(db.String(256), nullable=False)  # 不允许为空
    t_desc = db.Column(db.String(512))  # 简介 不允许为空
    t_image = db.Column(db.String(1024))  # 封面图
    t_url = db.Column(db.String(1024))  # 原文链接 先去掉
    t_cate = db.Column(db.String(8))  # 添加分类id 和 分类表关联
    total_click_count = db.Column(db.Integer)  # 总点击数
    current_click_count = db.Column(db.Integer)  # 当前点击数每天的点击量
    status = db.Column(db.SmallInteger, default="0")  # 任务状态(0关闭1开启2待审核-1已删除)
    memo = db.Column(db.VARCHAR(128))  # 备注
    t_key = db.Column(db.VARCHAR(164), unique=True)  # 唯一key 抓取文章源key
    t_read_count = db.Column(db.Integer)  # 文章阅读数
    t_time = db.Column(db.String(64), default=int(time.time() * 1000))  # 文章发布时间
    p_time = db.Column(db.String(64), default=int(time.time() * 1000))  # 推送时间
    article_type = db.Column(db.Integer, nullable=False)  # 1：普通类型 2：视频类型
    is_get = db.Column(db.Boolean, default=False)  # 是否已推送
    is_hot = db.Column(db.Boolean, default=False)  # 是否是热点
    video_second = db.Column(db.SmallInteger)  # 播放时长 毫秒
    video_url = db.Column(db.VARCHAR(255))  # 视频地址
    tags = db.Column(db.String(1024))  # 文章标签
    task_platform = db.Column(db.SmallInteger)  # 文章来源
    grad_read_count = db.Column(db.SmallInteger)  # 抓取阅读数
    grad_forward_count = db.Column(db.SmallInteger)  # 抓取转发数
    grad_comments_count = db.Column(db.SmallInteger)  # 抓取评论数

    def __init__(self, **kwargs):
        super(FanTask, self).__init__(**kwargs)

    def __repr__(self):
        return f"<FanTask: {self.t_title}>"


class FanTaskDetail(BaseModel, db.Model):
    """
    文章详情表
    """
    task_id = db.Column(db.Integer, nullable=False, primary_key=True)  # 文章id
    task_content = db.Column(db.Text, nullable=False)  # 文章内容
    task_comment = db.Column(db.Text)  # 文章评论区预留

    def __init__(self, **kwargs):
        super(FanTaskDetail, self).__init__(**kwargs)


class FanTaskAuthor(BaseModel, db.Model):
    """
    作者表
    """
    t_author = db.Column(db.String(256))  # 原文作者
    t_author_id = db.Column(db.String(64), primary_key=True)  # 作者id
    channel_id = db.Column(db.Integer)  # 作者来源id

    def __init__(self, **kwargs):
        super(FanTaskAuthor, self).__init__(**kwargs)


class FanUser(BaseModel, db.Model):
    """
    用户表
    """
    f_uid = db.Column(db.String(64), primary_key=True)   # 用户ID
    f_name = db.Column(db.String(128), nullable=False)   # 用户名
    f_password = db.Column(db.String(64), nullable=False)  # 密码 MD5
    f_role = db.Column(db.Integer)     # 用户角色级别 存储角色id
    f_email = db.Column(db.String(64))   # 邮箱用于找回密码

    def __init__(self, **kwargs):
        super(FanUser, self).__init__(**kwargs)


class FanRole(db.Model):
    """
    后台角色表
    """
    f_role_id = db.Column(db.String(64), primary_key=True)   # 角色id
    f_role_name = db.Column(db.String(128), nullable=False)  # 角色名称 如管理员  普通用户

    def __init__(self, **kwargs):
        super(FanRole, self).__init__(**kwargs)
