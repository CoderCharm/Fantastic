# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2018/12/17 10:15
# @Desc:
import click
from flask import Flask
# from app.extensions import db
# from flask_sqlalchemy import SQLAlchemy
from settings import DATA_BASE
from app.article import article as article_blueprint  # 导入蓝图

# def config_mysql(app):
#     """
#     数据库配置
#     :param app:
#     :return:
#     """
#     user = DATA_BASE.get("user")
#     password = DATA_BASE.get("password")
#     host = DATA_BASE.get("host")
#     data_name = DATA_BASE.get("data_name")
#     app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{user}:{password}@{host}/{data_name}"
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # 追踪
#     app.config['SECRET_KEY'] = '75aec5b16f558c35478c8fac339e4dbd'
#     db.init_app(app)
#
#
# def create_app():
#     app = Flask(__name__)  # 创建flask app对象
#     app.debug = True  # 调试模式
#     # 注册Blueprint
#     app.register_blueprint(article_blueprint)
#     config_mysql(app)
#
#     return app

app = Flask(__name__)  # 创建flask app对象
app.debug = True  # 调试模式
# 注册Blueprint
app.register_blueprint(article_blueprint)

from app.api.v1 import create_blueprint_v1
app.register_blueprint(create_blueprint_v1(), url_prefix='/api/v1')

user = DATA_BASE.get("user")
password = DATA_BASE.get("password")
host = DATA_BASE.get("host")
data_name = DATA_BASE.get("data_name")
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{user}:{password}@{host}/{data_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # 追踪
app.config['SECRET_KEY'] = '75aec5b16f558c35478c8fac339e4dbd'


@app.cli.command()  # 第五章 p594  用法>flask initdb <--drop>
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    from app.models import db
    if drop:  # 删除数据表
        click.confirm("This operation will delete databases, do you want to continue?", abort=True)
        db.drop_all()
        click.echo("Drop Tables")
    db.create_all()  # 初始化 建立数据表
    click.echo("Initialized DataBases.")
