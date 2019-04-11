# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:52
# @Desc: 
"""

"""
import click
from flask import Flask
from flask_cors import CORS

from models import db
from api.views import api
from settings import DATA_BASE


def create_app(config=None, testing=False, cli=False):
    """
    Application factory, used to create application
    :param config:
    :param testing:
    :param cli:
    :return:
    """
    app = Flask(__name__)

    register_blueprints(app)   # 注册蓝图
    config_mysql(app)          # 配置数据库
    db.init_app(app)           # 初始化app

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


def config_mysql(app):
    """
    mysql setting
    :param app:
    :return:
    """
    user = DATA_BASE.get("user")
    password = DATA_BASE.get("password")
    host = DATA_BASE.get("host")
    data_name = DATA_BASE.get("data_name")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{user}:{password}@{host}/{data_name}"
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 280  # 连接池
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  #
    app.config['SECRET_KEY'] = '75aec5b16f558c35478c8fac339e4dbd'
    # from app.models import db
    # # with app.app_context():
    # db.init_app(app)


from manage import application  # Command-line use init db


# TODO() don't move to the top.This will given error. and I don't know why?


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
