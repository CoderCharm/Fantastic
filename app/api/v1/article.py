# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/1/7 11:11
# @Desc: 
"""

"""
from flask import request, jsonify
from app.libs.redprint import RedPrint
from app.models import db, FanTask, FanTaskDetail
from sqlalchemy import exc   # 捕获异常

# from flask_restful import Resource 准备使用flask_restful的 但是不是很好加载 route 暂时不考虑
api = RedPrint('article')


@api.route('/get/list', methods=["GET"])
def get_article_list():
    """
    获取文章列表
    :return:
    """
    return jsonify({"param": request.args.get("abc")})


@api.route('/get/detail', methods=["GET"])
def get_article_detail():
    """
    获取文章详情
    :return:
    """
    return jsonify({"param": request.args.get("article_id")})


@api.route('/del', methods=["DELETE"])
def del_article():
    """
    删除文章
    :return:
    """
    return "success"


@api.route('/add', methods=["POST"])
def add_article():
    """
    添加文章
    :return:
    """
    t_author = request.form.get("t_author")
    t_title = request.form.get("t_title")
    t_desc = request.form.get("t_desc")
    t_image = request.form.get("t_image")
    t_url = request.form.get("t_url")
    t_key = request.form.get("t_key")
    article_type = request.form.get("article_type")
    task_content = request.form.get("t_content")

    article_list = FanTask(
        t_author=t_author,
        t_title=t_title,
        t_desc=t_desc,
        t_image=t_image,
        t_url=t_url,
        t_key=t_key,
        article_type=article_type
    )

    try:
        db.session.add(article_list)
        db.session.commit()
        article_detail = FanTaskDetail(task_id=article_list.task_id, task_content=task_content)
        db.session.add(article_detail)
        db.session.commit()
        return jsonify({"res": 1, "msg": "Success"})
    except exc.SQLAlchemyError:
        db.session.rollback()
        return jsonify({"res": -1, "msg": "Error"})

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# api.add_resource(HelloWorld, '/hello')
