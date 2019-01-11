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

@article.route("/news")  # 新闻详情页
def news():
    return render_template("news.html")