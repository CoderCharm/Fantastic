#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2018/12/17 10:12
# @Desc: main project file

from api import create_app
# from extensions import socketio

app = create_app("development")

if __name__ == '__main__':
    from datetime import datetime  #

    print("############# flask start {} ###########".format(datetime.utcnow()))
    # 打印两次原因
    # https://stackoverflow.com/questions/25504149/why-does-running-the-flask-dev-server-run-itself-twice
    print(app.url_map)  # 打印所有路由信息
    app.run(host="0.0.0.0", debug=True)
    # socketio.run(app, host="127.0.0.1", port="9999", debug=True)
