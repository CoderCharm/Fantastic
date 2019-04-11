# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:53
# @Desc: 
"""
路由管理
"""
from flask import Blueprint
from flask_restful import Api

from .v1.admin.user import Login
from .v1.article.index import List, Cate, Demo


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

# user operation
api.add_resource(Login, '/user/login')

# article operation
api.add_resource(Demo, '/article/<int:item_id>')
api.add_resource(List, '/article/get/list')
api.add_resource(Cate, '/article/get/cate')

