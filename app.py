#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2018/12/17 10:12
# @Desc: main project file
import click

from datetime import datetime  #

from api import create_app
from extensions import db

app = create_app("development")


@app.cli.command()  # p594  Usage>flask initdb <--drop>
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    """Initialize the database."""
    from api.models.user import FanRole
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    # 插入默认数据
    for name in ['普通用户', '管理员']:
        role = FanRole(f_role_name=name)
        db.session.add(role)
    db.session.commit()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--admin', is_flag=True, help='Create default admin account')
def createuser(admin):
    """
    创建系统用户
    Usage:
        > flask createuser  # 普通用户
        > flask createuser --admin  # 管理员
    :param admin:
    :return:
    """
    from api.models.user import FanUser, FanRole
    from uuid import uuid4
    if admin:
        print("🌟🌟✨创建管理员✨🌟🌟")
        # 默认
        role_name = "管理员"
        username = "admin"
        password = "123456"
    else:
        role_name = "普通用户"
        print("====创建普通用户===")
        username = input("输入用户名: ")
        password = input("输入密码: ")
    # 首先查询是否已创建
    admin_user = FanUser.query.filter_by(f_name=username).first()
    if admin_user:
        print(f"用户名 {username} 已存在！ 🔥️️请勿重复创建")
        return

    # 查询角色id
    role = FanRole.query.filter_by(f_role_name=role_name).first()
    user = FanUser(f_role=role.id, f_uid=str(uuid4()), f_name=username, f_password=password)
    user.hash_password(password)

    db.session.add(user)
    db.session.commit()
    print(f"用户:{username} 密码:{password}  👋*创建成功*👋")


if __name__ == '__main__':
    print("############# flask start {} ###########".format(
        datetime.utcnow()))  # 打印两次原因 https://stackoverflow.com/questions/25504149/why-does-running-the-flask-dev-server-run-itself-twice
    print(app.url_map)  # 打印所有路由信息
    app.run(host="0.0.0.0", debug=True)
