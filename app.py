#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2018/12/17 10:12
# @Desc: main project file
# from app import create_app
import click

from api import create_app
from datetime import datetime  #

app = create_app("development")


@app.cli.command()   # p594  Usage>flask initdb <--drop>
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    """Initialize the database."""
    from extensions import db
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort = True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')


if __name__ == '__main__':
    print("############# flask start {} ###########".format(datetime.utcnow())) # 打印两次原因 https://stackoverflow.com/questions/25504149/why-does-running-the-flask-dev-server-run-itself-twice
    print(app.url_map)  # 打印所有路由信息
    app.run(debug=True)
