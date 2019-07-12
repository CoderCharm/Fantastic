# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:51
# @Desc: 
"""

"""
from flask import Flask
from extensions import CORS, db

from config import config
# from api.models.admin import db
from api.v1_views import api as api_v1


def create_app(config_name):
    """
    Application factory, used to create application
    :param config_name:
    :return:
    """
    app = Flask(__name__)

    register_blueprints(app)  # 注册蓝图

    # 配置数据库
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)  # 初始化app

    # 跨域
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    return app


def register_blueprints(app):
    """
    register all blueprints for application
    :param app:
    :return:
    """
    app.register_blueprint(api_v1.blueprint)


