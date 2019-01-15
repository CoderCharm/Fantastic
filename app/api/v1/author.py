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
	# 根据作者id查询作者的头像和文章
	# 接收的参数
	# 实现分页查询的功能 page 页数 size 一页显示的数据 cate 分类查询
	page = request.args.get('page', 1, type=int)
	size = request.args.get('size', 20, type=int)
	author_id = request.args.get('author_id', '', type=int)
	page = (int(page) - 1) * 10
	info_res = FanTask.query.filter(FanTask.t_author_id == author_id).order_by(FanTask.task_id.desc()).offset(
		page).limit(size)
	data_list = []
	for info in info_res:
		tmp = {
			"account": {
				"avatar": info.t_author_img,
				"description": "",
				"id": author_id,
				"nickname": info.t_author,
			},
			"content_url": info.t_url,
			"copyright_stat": 11,
			"cover": info.t_image,
			"digest": info.t_desc,
			"id": 10723,
			"md5_url": info.uuid,
			"published_at": time.strftime("%Y-%m-%d", time.localtime(int(info.create_time[:-3]))),
			"title": info.t_title,
			"top": 0,
			
		}
		
		data_list.append(tmp)
	
	data = {"code": 200, "count": 564,
	        "data": data_list,
	        "msg": "success",
	        "page": page,
	        "size": size,
	        }
	return jsonify(data)
