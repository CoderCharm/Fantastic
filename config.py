# -*- coding:utf-8 -*-
# @Author: wgPython
# @Time: 2019/2/16 17:01
# @Desc: 
"""
配置文件  未使用

"""


class Config(object):
    SECRET_KEY = "75aec5b16f558c35478c8fac339e4dbd"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class MySQLConfig(object):
    MYSQL_USERNAME = 'bingbing'
    MYSQL_PASSWORD = '123456'
    MYSQL_HOST = '39.105.119.228'


class DevelopmentConfig(Config):
    DEBUG = True
    database = 'fantastic'
    SQLALCHEMY_DATABASE_URI = f"mysql://{MySQLConfig.MYSQL_USERNAME}:{MySQLConfig.MYSQL_PASSWORD}@" \
                              f"{MySQLConfig.MYSQL_HOST}/{database}"


class TestingConfig(Config):
    TESTING = True
    database = 'mysql_test'
    SQLALCHEMY_DATABASE_URI = f"mysql://{MySQLConfig.MYSQL_USERNAME}:{MySQLConfig.MYSQL_PASSWORD}@" \
                              f"{MySQLConfig.MYSQL_HOST}/{database}"


class ProductionConfig(Config):
    database = 'fantastic'
    SQLALCHEMY_DATABASE_URI = f"mysql://{MySQLConfig.MYSQL_USERNAME}:{MySQLConfig.MYSQL_PASSWORD}@" \
                              f"{MySQLConfig.MYSQL_HOST}/{database}"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig  # 默认开发环境
}
