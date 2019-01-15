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
	"""查询作者详情页
		---
		tags:
		  - Articles API
		parameters:
		  - name: page
			in: path
			type: integer
			required: false
			default: 1
			description: 数据起页坐标
		  - name: size
			in: query
			type: integer
			required: false
			default: 10
			description: 每次数据长度
		  - name: cate
			in: query
			type: string
			required: false
			default: null
			description: 数据分类
		responses:
		  200:
			description: 返回新闻数据信息
			examples:
			  {"cate":"Null","code":200,"count":2,"data":[{"account":{"avatar":"作者头像","id":89,"nickname":"源昵称","qrcode":null},"author":"作者昵称","content_url":"源链接","copyright_stat":11,"cover":"封面图","digest":"简介","id":10723,"md5_url":"7f156a7a17a111e9ba69005056c00002","published_at":"2019-01-14","title":"标题","top":0},{"account":{"avatar":"http://p3.pstatp.com/thumb/ffa600000d7c58105a0e","id":89,"nickname":"\u641e\u7b1128\u5929","qrcode":null},"author":"\u641e\u7b1128\u5929","content_url":"http://toutiao.com/group/6645819586602074627/","copyright_stat":11,"cover":"http://p1-tt.bytecdn.cn/list/300x196/pgc-image/4ef6ece303a641f896c65234de3e7adc.webp","digest":"\u90fd\u662f\u4e5d\u5e74\u4e49\u52a1\u6559\u80b2\uff0c\u4e3a\u4ec0\u4e48\u4f60\u5982\u6b64\u4f18\u79c0\u54e5\u4eec\uff0c\u4f60\u662f\u7334\u5b50\u8bf7\u6765\u7684\u9017\u6bd4\u5417\u5176\u5b9e\u6211\u4e0d\u662f\u4e00\u53cc\u978b\u5b50","id":10723,"md5_url":"7f156a7a17a111e9ba69005056c00002","published_at":"2019-01-14","title":"\u7537\u4eba\u6dd8\u5b9d\u4e70\u5bb6\u79c0\uff0c\u5143\u82b3\u4f60\u600e\u4e48\u770b\uff0c\u5143\u82b3\uff1a\u201c\u6211\u9000\u94b1\u60a8\u53ef\u4ee5\u5220\u9664\u5417\uff1f\u201d","top":0},],"msg":"success","page":2,"size":10}

		"""

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
