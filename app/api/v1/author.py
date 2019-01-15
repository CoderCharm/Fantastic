# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/1/15 17:46
# @Desc: 
"""

"""
from flask import request, jsonify
from app.libs.redprint import RedPrint
from app.models import db, FanTask, FanTaskDetail, FanTaskCate
from sqlalchemy import exc  # 捕获异常
import time

api = RedPrint('author')


@api.route('/get/list', methods=["GET"])
def author_info():
    author_id = request.args.get('author_id')
    return jsonify({"author": author_id})
