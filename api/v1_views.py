# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:53
# @Desc: 
"""
路由管理
"""
from flask import Blueprint, request, redirect
from flask_restful import Api

from api.models.user import FanUser
from extensions import swagger
from .v1.auth.user import AuthUser  # 认证
from .v1.article.index import ArticleList, ArticleCate, Demo  # 文章
from .v1.article.charts import ChartsCate
from .v1.utils.upload import UpLoad  # 工具类操作

# 蓝图注册前缀
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)
api = swagger.docs(api, apiVersion='0.1')


@api.app.before_request
def before_req():
    """
    钩子函数 确定
    :return:
    """
    print('===', request.path)
    if request.path.endswith('/auth'):
        pass
    else:
        # 非登陆url 验证token
        print("🌹" * 10)
        authentication = request.headers.get("Authentication")
        if not authentication:
            # 没有获取到authentication
            return {"code": 400, "msg": "未认证, 请重新认证"}
        if not FanUser.verify_auth_token(authentication):
            return {"code": 400, "msg": "未认证, 请重新认证"}


# user operation
api.add_resource(AuthUser, '/user/auth')

# article operation
api.add_resource(Demo, '/article/<int:item_id>')
api.add_resource(ArticleList, '/article/get/list')
api.add_resource(ArticleCate, '/article/get/cate')

# data charts operation
api.add_resource(ChartsCate, '/Charts/get/cate')  # 获取分类统计数据

# other utils
api.add_resource(UpLoad,
                 # '/picture/<path:path>',  # get请求获取图片  直接使用static文件夹就行
                 '/picture/upload',  # 响应 post请求 上传图片
                 )
