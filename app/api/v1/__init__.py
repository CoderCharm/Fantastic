# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/1/7 11:09
# @Desc: 
"""
api 接口文件  添加自定义红图
"""
from flask import Blueprint
from app.api.v1 import article


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    article.api.register(bp_v1)

    return bp_v1
