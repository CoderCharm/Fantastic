# -*- coding:utf-8 -*-
# @Author: wgPython
# @Time: 2018/12/17 10:15
# @Desc:
import click
from flask import Flask
from flasgger import Swagger
from settings import DATA_BASE


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
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  #
    app.config['SECRET_KEY'] = '75aec5b16f558c35478c8fac339e4dbd'
    from app.models import db
    db.init_app(app)


def create_app():
    app = Flask(__name__)  # create flask app obj
    app.debug = True  # debug model
    # Register Blueprint
    from app.article import article as article_blueprint  # import blueprint
    app.register_blueprint(article_blueprint)
    from app.api.v1 import create_blueprint_v1  # import my define RedPrint
    app.register_blueprint(create_blueprint_v1(), url_prefix='/api/v1')
    config_mysql(app)
    Swagger(app)
    return app


from manage import app   # Command-line use init db
# TODO() don't move to the top.This will given error. and I don't know why?


@app.cli.command()  # p594  Usage>flask initdb <--drop>
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    from app.models import db
    if drop:  # drop databases tables
        click.confirm("This operation will delete databases, do you want to continue?", abort=True)
        db.drop_all()
        click.echo("Drop Tables")
    db.create_all()  # initialized DataBases
    click.echo("Initialized DataBases.")
