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
from .v1.article.index import ArticleList, ArticleCate, Demo  # 文章
from .v1.article.charts import ChartsCate
from .v1.utils.upload import UpLoad  # 工具类操作


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

# user operation
api.add_resource(Login, '/user/login')

# article operation
api.add_resource(Demo, '/article/<int:item_id>')
api.add_resource(ArticleList, '/article/get/list')
api.add_resource(ArticleCate, '/article/get/cate')

# data charts operation
api.add_resource(ChartsCate, '/Charts/get/cate')   # 获取分类统计数据

# other utils
api.add_resource(UpLoad,
                 # '/picture/<path:path>',  # get请求获取图片  直接使用static文件夹就行
                 '/picture/upload',         # 响应 post请求 上传图片
                 )

