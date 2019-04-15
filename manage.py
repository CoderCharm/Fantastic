# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2018/12/17 10:12
# @Desc: main project file
# from app import create_app
from api import create_app
from datetime import datetime  #

application = create_app("development")


# @application.errorhandler(404)
# def error_404(e):
#     return '404 Error', 404
#
#
# @application.errorhandler(Exception)
# def error_all(e):
#     return 'Error', 500


if __name__ == '__main__':
    print("############# flask start {} ###########".format(datetime.utcnow()))  # 打印两次原因 https://stackoverflow.com/questions/25504149/why-does-running-the-flask-dev-server-run-itself-twice
    print(application.url_map)  # 打印所有路由信息
    application.run(port=8000)
