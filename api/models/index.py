#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 10:12
# @Author  : wgPython
# @File    : index.py
# @Software: PyCharm
# @Desc    :
"""

"""
import time
from extensions import db


class BaseModel(object):
    """
    模型基类，为每个模型补充创建时间与更新时间
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.String(64), index=True, default=int(time.time() * 1000), comment="创建时间")  # index给定索引
    update_time = db.Column(db.String(64), default=int(time.time() * 1000), comment="更新时间")  # 记录的更新时间
    is_delete = db.Column(db.Boolean, default=False, comment="是否删除")

