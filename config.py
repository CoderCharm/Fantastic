# -*- coding:utf-8 -*-
# @Author: wgPython
# @Time: 2019/2/16 17:01
# @Desc: 
"""
配置文件
一般

"""


class Config(object):
    SECRET_KEY = "75aec5b16f558c35478c8fac339e4dbd"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class MySQLConfig(object):
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = 'phpPython@123Java-.-'
    MYSQL_HOST = '106.12.24.154'


class DevelopmentConfig(Config):
    DEBUG = True
    HOST_NAME = "http://127.0.0.1:8000"
    database = 'fantastic'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MySQLConfig.MYSQL_USERNAME}:{MySQLConfig.MYSQL_PASSWORD}@" \
                              f"{MySQLConfig.MYSQL_HOST}/{database}"


class TestingConfig(Config):
    TESTING = True
    HOST_NAME = ""
    database = 'mysql_test'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MySQLConfig.MYSQL_USERNAME}:{MySQLConfig.MYSQL_PASSWORD}@" \
                              f"{MySQLConfig.MYSQL_HOST}/{database}"


class ProductionConfig(Config):
    database = 'fantastic'
    HOST_NAME = ""
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MySQLConfig.MYSQL_USERNAME}:{MySQLConfig.MYSQL_PASSWORD}@" \
                              f"{MySQLConfig.MYSQL_HOST}/{database}"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig  # 默认开发环境
}

UA_WEB_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; NMTE; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
]

