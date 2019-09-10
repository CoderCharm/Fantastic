# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:51
# @Desc: 
"""

"""

import click

from flask import Flask, request

from config import config
from api.v1_views import api_v1
from api.v2_views import api_v2
from extensions import CORS, db


def create_app(config_name):
    """
    Application factory, used to create application
    :param config_name:
    :return:
    """
    app = Flask(__name__)

    # 配置数据库
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_extensions(app)  # 注册扩展
    register_blueprints(app)  # 注册蓝图
    register_commands(app)  # 注册自定义命令
    register_request(app)

    return app


def register_extensions(app):
    """注册扩展"""

    db.init_app(app)

    # socketio.init_app(app)
    # 跨域
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


def register_blueprints(app):
    """
    register all blueprints for application
    :param app:
    :return:
    """
    app.register_blueprint(api_v1.blueprint)
    app.register_blueprint(api_v2.blueprint)


def register_request(app):
    """注册通用请求"""
    from api.models.user import FanUser

    @app.before_request
    def before_req():
        """
        钩子函数 确定是否认证
        :return:
        """
        print('===', request.path)
        if request.path.endswith('/auth'):
            pass
        else:
            # 非登陆url 验证token
            print("🙈" * 10)
            authentication = request.headers.get("Authentication")
            if not authentication:
                # 没有获取到authentication
                return {"code": 400, "msg": "未认证, 请重新认证"}
            if not FanUser.verify_auth_token(authentication):
                return {"code": 401, "msg": "认证过期, 请重新认证"}


def register_commands(app):
    """注册自定义命令"""

    @app.cli.command()  # p594  Usage>flask initdb <--drop>
    @click.option('--drop', is_flag=True, help='Create after drop')
    def initdb(drop):
        """Initialize the database.
        Usage:
            > flask initdb    # 创建数据表
            > flask initdb --drop  # 删除之前数据表

        """
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
            > flask createuser  # 创建普通用户
            > flask createuser --admin  # 创建管理员
        :param admin:
        :return:
        """
        from api.models.user import FanUser, FanRole
        from uuid import uuid4
        if admin:
            print("🌟🌟✨创建管理员✨🌟🌟")
            # 默认
            role_name = "管理员"
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
        print(f"用户:{username} 密码:{password}  👋* {role_name} 创建成功*👋")
