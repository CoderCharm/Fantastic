#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 12:00
# @Author  : wgPython
# @File    : serialize.py
# @Software: PyCharm
# @Desc    :
"""
序列化， 定义常规的数据返回
"""

from flask_restful import fields

resp_200_fields = {
    'code': fields.Integer(default=200),
    'msg': fields.String(default="ok"),
    'data': fields.String,
}

resp_404_fields = {
    'code': fields.Integer(default=404),
    'msg': fields.String(default="Page Not Found"),
    'data': fields.String,
}

resp_500_fields = {
    'code': fields.Integer(default=500),
    'msg': fields.String(default="Server internal error"),
    'data': fields.String,
}
