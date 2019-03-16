# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:53
# @Desc: 
"""

"""
from flask import Blueprint
from flask_restful import Api

from .v1.article import ArticleResource, ArticleList


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(ArticleList, '/article')

api.add_resource(ArticleResource, '/article/<int:item_id>')