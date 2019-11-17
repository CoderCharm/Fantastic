# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/3/16 14:51
# @Desc: 
"""

"""
import os
import click

from flask import Flask

from config import config
from api.v1_views import api_v1
from api.v2_views import api_v2
from extensions import CORS, db, scheduler


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
    register_exception(app)
    register_logging(app)

    return app


def register_extensions(app):
    """注册扩展"""

    db.init_app(app)

    scheduler.init_app(app)

    scheduler.start()
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

    # @app.before_request
    # def before_req():
    #     """
    #     钩子函数 确定是否认证
    #     :return:
    #     """
    #     print('request.path===', request.path)
    #     if not request.path.endswith('/auth'):
    #         # 非登陆url 验证token
    #         print("🙈" * 10)
    #         authentication = request.headers.get("Authentication")
    #         if not authentication:
    #             # 没有获取到authentication
    #             return {"code": 400, "msg": "未认证, 请重新认证"}
    #         if not FanUser.verify_auth_token(authentication):
    #             return {"code": 401, "msg": "认证过期, 请重新认证"}


def register_exception(app):
    """捕获全局异常"""
    from flask_restful import marshal_with
    from utils.serialize import resp_404_fields, resp_500_fields

    @app.errorhandler(404)
    @marshal_with(resp_404_fields)
    def error_404(e):
        return

    @app.errorhandler(Exception)
    @marshal_with(resp_500_fields)
    def all_exception_handler(e):
        return


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
        print(f"用户:{username}\n密码:{password}  👋* {role_name} 创建成功*👋")


def register_logging(app):
    """
    logging setting
    :param app:
    :return:
    """
    import logging
    from logging.handlers import RotatingFileHandler

    class InfoFilter(logging.Filter):
        def filter(self, record):
            """only use INFO
            筛选, 只需要 INFO 级别的log
            :param record:
            :return:
            """
            if logging.INFO <= record.levelno < logging.ERROR:
                # 已经是INFO级别了
                # 然后利用父类, 返回 1
                return super().filter(record)
            else:
                return 0

    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 定位到log日志文件
    log_path = os.path.join(basedir, 'logs')

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    log_path_error = os.path.join(log_path, 'error.log')
    log_path_info = os.path.join(log_path, 'info.log')
    # log_file_max_bytes = 100 * 1024 * 1024
    # # 轮转数量是 10 个
    # log_file_backup_cpunt = 10

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(process)d %(thread)d '
        '%(pathname)s %(lineno)s %(message)s')

    # FileHandler Info
    file_handler_info = RotatingFileHandler(filename=log_path_info)
    file_handler_info.setFormatter(formatter)
    file_handler_info.setLevel(logging.INFO)
    info_filter = InfoFilter()
    file_handler_info.addFilter(info_filter)
    app.logger.addHandler(file_handler_info)

    # FileHandler Error
    file_handler_error = RotatingFileHandler(filename=log_path_error)
    file_handler_error.setFormatter(formatter)
    file_handler_error.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler_error)