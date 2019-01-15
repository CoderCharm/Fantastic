# -*- coding:utf-8 -*-
# @Author: wgPython
# @Time: 2019/1/7 11:11
# @Desc: 
"""

"""
from flask import request, jsonify
from app.libs.redprint import RedPrint
from app.models import db, FanTask, FanTaskDetail, FanTaskCate
from sqlalchemy import exc  # 捕获异常
import time

# from flask_restful import Resource 准备使用flask_restful的 但是不是很好加载 route 暂时不考虑
api = RedPrint('article')


@api.route('/get/list', methods=["GET"])
def get_article_list():
	"""查询文章接口每次返回10条数据
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
	# 实现分页查询的功能 page 页数 size 一页显示的数据 cate 分类查询
	page = request.args.get('page', 1, type=int)
	size = request.args.get('size', 20, type=int)
	cate = request.args.get('cate', '', type=int)
	pages = (int(page) - 1) * 10
	# 判断是否有分类
	if cate:
		info_res = FanTask.query.filter(FanTask.t_cate == cate).order_by(FanTask.task_id.desc()).offset(pages).limit(
			size)
	else:
		info_res = FanTask.query.order_by(FanTask.task_id.desc()).offset(pages).limit(size)
	data_list = []
	for info in info_res:
		tmp = {"account": {
			"avatar": info.t_author_img,
			"id": 89, "nickname": info.t_author, "qrcode": None},
			"author": info.t_author,
			"content_url": info.t_url,
			"copyright_stat": 11,
			"cover": info.t_image,
			"digest": info.t_desc,
			"id": 10723,
			"md5_url": info.uuid,
			"published_at": time.strftime("%Y-%m-%d", time.localtime(int(info.create_time[:-3]))),
			"title": info.t_title,
			"top": 0
		}
		
		data_list.append(tmp)
	
	data = {"code": 200, "count": 564,
	        "data": data_list,
	        "cate": cate,
	        "msg": "success",
	        "page": page,
	        "size": size,
	        }
	
	return jsonify(data)


# 类目api
@api.route('/get/cate', methods=["GET"])
def get_article_cate():
	"""返回接口分类
		---
		tags:
		  - Articles API
		responses:
		  200:
			description: 返回接口分类
			examples:
			  {"cate_list":[{"cate_id":1,"cate_name":"\u641e\u7b11"},{"cate_id":2,"cate_name":"\u79d1\u6280"},{"cate_id":3,"cate_name":"\u52b1\u5fd7"}],"code":200}

	"""
	cate_info = FanTaskCate.query.all()
	cate_list = []
	for info in cate_info:
		cate = {
			"cate_id": info.cate_id,
			'cate_name': info.cate_name,
		}
		cate_list.append(cate)
	data = {
		"code": 200,
		'cate_list': cate_list,
	}
	return jsonify(data)


@api.route('/get/detail', methods=["GET"])
def get_article_detail():
	"""文章内容接口
	---
		tags:
		  - Articles API
		parameters:
		  - name: uuid
			in: path
			type: string
			enum: 1
			required: true
			default: 1
			description: 详情页的uuid
		responses:
		  200:
			description: 返回新闻数据信息
			examples:

	"""
	# 根据uid查询内容：标题，标签
	uuid = request.args.get('uuid')
	print(uuid)
	info_res = FanTask.query.filter(FanTask.uuid == uuid).all()
	
	# info_news = FanTaskDetail.query.filter(FanTask.uuid == uuid).all()
	src = {}
	for info in info_res:
		
		src['title'] = info.t_title
		src['grad_read_count'] = info.grad_read_count
		
		# 作者
		src['t_author'] = info.t_author
		# 文章发布时间
		src['t_time'] = time.strftime("%Y-%m-%d", time.localtime(int(info.t_time[:-3])))
		t_cate = int(info.t_cate)
		if t_cate == 1:
			print('---')
			cates = '搞笑'
		elif t_cate == 2:
			cates = '科技'
		elif t_cate == 3:
			cates = '励志'
		src['cate'] = cates
		
		print(t_cate)
		task_id = info.task_id
	
	info_news = FanTaskDetail.query.filter(FanTaskDetail.task_id == task_id).all()
	for info in info_news:
		src['nes_content'] = info.task_content
	data = {"code": 200,
	        "data": src, }
	return jsonify(data)


@api.route('/del', methods=["DELETE"])
def del_article():
	"""
	delete article by uuid  TODO(wgPython) Privilege Authentication Not Implemented
	:return:
	"""
	return "success"


# 精选编辑接口
@api.route('/featured')
def get_featured():
	# 前面有相关的接口就多了一个状态
	# status任务状态(0关闭1开启2待审核-1已删除) 自己手动修改
	info_res = FanTask.query.order_by(FanTask.task_id.desc()).filter(FanTask.status == 1).limit(4)
	data_list = []
	for info in info_res:
		tmp = {"account": {
			"avatar": info.t_author_img,
			"id": 89, "nickname": info.t_author, "qrcode": None},
			"author": info.t_author,
			"content_url": info.t_url,
			"copyright_stat": 11,
			"cover": info.t_image,
			"digest": info.t_desc,
			"id": 10723,
			"md5_url": info.uuid,
			"published_at": time.strftime("%Y-%m-%d", time.localtime(int(info.create_time[:-3]))),
			"title": info.t_title,
			"top": 0
		}
		
		data_list.append(tmp)
	
	data = {"code": 200, "count": 564,
	        "data": data_list,
	        "msg": "success",
		
	        }
	
	return jsonify(data)


# 作者接口
@api.route('/author')
def author():
	pass


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
	t_cate = request.form.get("t_cate")
	t_key = request.form.get("t_key")
	article_type = request.form.get("article_type")
	task_content = request.form.get("t_content")
	user_id = request.form.get("user_id")
	article_list = FanTask(
		t_author=t_author,
		t_title=t_title,
		t_cate=t_cate,
		t_desc=t_desc,
		t_image=t_image,
		t_url=t_url,
		t_key=t_key,
		article_type=article_type,
		user_id=user_id
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
