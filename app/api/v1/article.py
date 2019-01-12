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
	""" 查询文章接口每次返回10条数据
	
		tags:
		  - Articles API
		parameters:
		  - name: page
			in: path
			type: string
			enum: 1
			required: true
			default: 1
			description: 数据起页坐标
		  - name: size
			in: path
			type: string
			enum: 10
			required: true
			default: 10
			description: 每次数据长度
		responses:
		  200:
			description: 返回新闻数据信息
			examples:
			  data: {"code":200,"count":564,"data":[{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/e22dbb9947d65f1e80d0774dac042eaf6df2a651.jpg","description":"有内容的技术社区媒体","id":89,"nickname":"InfoQ","qrcode":null},"author":"望京一哥小智","content_url":"http://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651012453&idx=1&sn=5aa8355f1ba86ab346c3d7910c91791b&chksm=bdbec5368ac94c20544c7258e0fc64e9ace4943e0182a6224cbe5b0dd03966b4307778b351a2&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/46401ac95baad5d9d291b2008f35b2302d4c7d39.jpg","digest":"如果用一句话形容你的 2018，会是什么？如果用一句话预测你的 2019，又会是什么？","id":10723,"md5_url":"de1d512dc11c8ccb21362d2c33540e54","published_at":"2019-01-06T10:31:55","title":"程序员2018年度代码报告，句句戳心","top":0}],"msg":"success","page":2,"size":10}
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
	"""
	所要传的参数uuid
	获取文章详情
	:return:
	"""
	# 根据uid查询内容：标题，标签
	uuid = request.args.get('uuid')
	print(uuid)
	info_res = FanTask.query.filter(FanTask.uuid == uuid).all()
	info_news = FanTaskDetail.query.filter(FanTask.uuid == uuid).all()
	src = {}
	for info in info_res:
		src['title'] = info.t_title
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
	
	article_list = FanTask(
		t_author=t_author,
		t_title=t_title,
		t_cate=t_cate,
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
