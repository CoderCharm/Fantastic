# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:53
# @Desc: 
"""
路由管理
"""
from flask import Blueprint
from flask_restful import Api

from .v1.admin.user import Login   # 后台
from .v1.article.index import List, Cate, Demo  # 文章
from .v1.utils.upload import UpLoad


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

# user operation
api.add_resource(Login, '/user/login')

# article operation
api.add_resource(Demo, '/article/<int:item_id>')
api.add_resource(List, '/article/get/list')
api.add_resource(Cate, '/article/get/cate')

# other utils
api.add_resource(UpLoad,
                 # '/picture/<path:path>',  # get请求获取图片  直接使用static文件夹就行
                 '/picture/upload',         # 响应 post请求 上传图片
                 )

