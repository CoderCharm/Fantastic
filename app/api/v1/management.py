# -*- coding:utf-8 -*-
# @Author: wyb
# @Time: 2019/1/24 11:18
# @Desc:
"""

"""
from flask import request, jsonify
from app.libs.redprint import RedPrint
from app.models import db, FanTask, FanTaskDetail, FanTaskCate, FanTaskAuthor
from sqlalchemy import exc  # 捕获异常
import time

api = RedPrint('management')


# 修改文章状态的接口
@api.route('/news/modify', methods=["GET"])
def news_update():
	status = request.args.get('status')
	task_id = request.args.get('task_id')
	blog = FanTask.query.filter_by(task_id=task_id).update({'status': status})
	# 提交才生效
	db.session.commit()
	if status == 1:
		status = '已发布'
	elif status == 0:
		status = '审核中'
	elif status == -1:
		status = '已拒绝'
	else:
		status = '参数不对'
	data = {
		'code': 200,
		'msg': status
	}
	return jsonify(data)


# 后台文章接口
@api.route('/news/Inquire', methods=["GET"])
def news_status():
	'''
	请求接口 http://127.0.0.1:8000/api/v1/management/news/Inquire?page=1&size=30&status=0
	:return:
	'''
	page = request.args.get('page', 1, type=int)
	size = request.args.get('size', 30, type=int)
	status = request.args.get('status', 5, type=int)
	pages = (int(page) - 1) * 10
	# 判断是否有分类
	print(status)
	if status == 5:
		info_res = FanTask.query.offset(pages).limit(size)
	
	else:
		print('---------------------------')
		info_res = FanTask.query.filter(FanTask.status == status).offset(pages).limit(
			size)
	data_list = []
	for info in info_res:
		if info.status == 1:
			status = '已发布'
		elif info.status == 0:
			status = '审核中'
		elif info.status == -1:
			status = '已拒绝'
		else:
			status = '参数不对'
		tmp = {
			"author": info.t_author,  # 原文作者
			'author_id': info.t_author_id,  # 作者id
			"content_url": info.t_url,  # 原文连接
			"cover": info.t_image,  # 封面图
			"md5_url": info.uuid,  # 文章MD5加密接口
			"published_at": time.strftime("%Y-%m-%d", time.localtime(int(info.create_time[:-3]))),  # 抓取时间
			"title": info.t_title,  # 文章表题
			"status": status,  # 文章的状态# 任务状态(0关闭1开启2待审核-1已删除)
		}
		
		data_list.append(tmp)
	
	data = {"code": 200, "count": 564,
	        "data": data_list,
	        "msg": "success",
	        "page": page,
	        "size": size,
	        }
	
	return jsonify(data)
	




