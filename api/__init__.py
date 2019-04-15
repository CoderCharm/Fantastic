# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:51
# @Desc: 
"""

"""
import click

from flask import Flask
from flask_cors import CORS

from config import config
from models import db
from api.views import api


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
    app.register_blueprint(api.blueprint)


from manage import application  # Command-line use init db


# don't move to the top.This will given error.
@application.cli.command()  # p594  Usage>flask initdb <--drop>
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    from models import db
    if drop:  # drop databases tables
        click.confirm("This operation will delete databases, do you want to continue?", abort=True)
        db.drop_all()
        click.echo("Drop Tables")
    db.create_all()  # initialized DataBases
    click.echo("Initialized DataBases.")
