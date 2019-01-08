# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2018/12/17 10:12
# @Desc: 主项目文件
from app import app
# import click
# from app.extensions import db
# from app.models import *
from datetime import datetime  #


if __name__ == '__main__':
    print(
        f"############# flask start {datetime.utcnow()} ###########")  # 打印两次原因 https://stackoverflow.com/questions/25504149/why-does-running-the-flask-dev-server-run-itself-twice
    print(app.url_map)  # 打印所有路由信息
    # manager.run()
    # channel_name = FanTaskDetail(33, "内容33", "评论33")
    # db.session.add(channel_name)
    # 更改
    # db.session.query(FanTaskDetail).filter_by(task_id=22).update({'task_content': '内容被修改'})
    # # print(channel_name.task_id)  # None
    # db.session.commit()
    # print(channel_name.task_id)
    app.run(port=8000)
