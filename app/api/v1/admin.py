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
import platform
import os
import sys
from scrapy.cmdline import execute

api = RedPrint('admin')
def scas():
	sys.path.append(os.path.dirname(os.path.abspath(__file__)))
	execute(["scrapy", "crawl", "toutiao"])

@api.route('/scrapy', methods=["GET"])
def admin_info():
	#获取所有在的系统和python的版本
	system = platform.system()
	print(system)
	if system == 'Windows':
		scas()
		# a = os.system('scrapy crawl toutiao')
	#python的版本
	python_system = platform.python_version()
	print(python_system)
	return 'ssssssssssssssss'



