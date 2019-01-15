# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2018/12/21 16:28
# @Desc: 
"""

"""
from . import article  # 导入Blueprint对象
from flask import render_template, redirect, url_for


# url_for('static', filename='style.css')


@article.route("/")  # 指定默认路由
def index():
	return render_template("article/index.html")


# 详情页页面
@article.route('/article/detail/<task_id>', methods=['GET'])
def test(task_id):
	return render_template('article/news.html')


# 作者页面
@article.route('/author/<author_id>', methods=['GET'])
def author(author_id):
	return render_template('article/author.html')


# 后续功能
# 登录注册页面
@article.route("/login")
def login():
	return render_template('login.html')
	pass
