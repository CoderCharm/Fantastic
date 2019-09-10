# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:53
# @Desc: 
"""
路由管理
"""
from flask import Blueprint
from flask_restful import Api

from extensions import swagger
from .v1.auth.user import AuthUser  # 认证
from .v1.article.index import ArticleList, ArticleCate, Demo  # 文章
from .v1.article.charts import ChartsCate
from .v1.utils.upload import UpLoad  # 工具类操作

# 蓝图注册前缀
blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1 = Api(blueprint)
api_v1 = swagger.docs(api_v1, apiVersion='0.1')

# @api_v1.app.before_request


# user operation
api_v1.add_resource(AuthUser, '/user/auth')

# article operation
api_v1.add_resource(Demo, '/article/<int:item_id>')
api_v1.add_resource(ArticleList, '/article/get/list')
api_v1.add_resource(ArticleCate, '/article/get/cate')

# data charts operation
api_v1.add_resource(ChartsCate, '/Charts/get/cate')  # 获取分类统计数据

# other utils
api_v1.add_resource(UpLoad,
                    # '/picture/<path:path>',  # get请求获取图片  直接使用static文件夹就行
                    '/picture/upload',  # 响应 post请求 上传图片
                    )
