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
		- name: cate
			in: path
			type: string
			enum: 10
			required: true
			default: 10
			description: 类目id
		responses:
		  200:
			description: 返回新闻数据信息
			examples:
				"data": {"account": {"avatar": "http://p3.pstatp.com/thumb/9b1f000397a099894aa6","id": 89,"nickname": "开心漫画","qrcode": null},"author": "开心漫画","content_url": "http://toutiao.com/group/6645851534548533767/","copyright_stat": 11,"cover": "http://p3-tt.bytecdn.cn/list/300x196/pgc-image/669fc0da9b6c4f5c9e54a8b4f588a5d7.webp","digest": "漫画：你以为我下不去手么","id": 10723,"md5_url": "f98f77d817a011e9bee5005056c00002","published_at": "2019-01-14","title": "漫画：你以为我下不去手么","top": 0},{"account": {"avatar": "http://p9.pstatp.com/thumb/a14b00043058e962ea0e","id": 89,"nickname": "欢乐集中谈","qrcode": null},"author": "欢乐集中谈","content_url": "http://toutiao.com/group/6645984282944750094/","copyright_stat": 11,"cover": "http://p9-tt.bytecdn.cn/list/300x196/pgc-image/828c1b9bd5104e72ae31d9b2ee8ad08d.webp","digest": "东西掉到地上三秒钟内马上捡起来可以吃的如果旁边没人时间还可以延长[/cp]​​​[cp]@劝分:掉地上都不忘拍照。","id": 10723,"md5_url": "f66fdca417a011e9a9af005056c00002","published_at": "2019-01-14","title": "爆笑朋友圈系列，这可能是今年最惨烈的现场了吧！掌众金融","top": 0},{"account": {"avatar": "http://p3.pstatp.com/thumb/d280000c0e230762aa0c","id": 89,"nickname": "嘀得哩嘀","qrcode": null},"author": "嘀得哩嘀","content_url": "http://toutiao.com/group/6645886971505803790/","copyright_stat": 11,"cover": "http://p1-tt.bytecdn.cn/list/300x196/pgc-image/74db831a0f4242e59686ac3fbe470014.webp","digest": "严冬的残雪","id": 10723,"md5_url": "edfb205217a011e9ae42005056c00002","published_at": "2019-01-14","title": "严冬的残雪","top": 0},{"account": {"avatar": "http://p1.pstatp.com/thumb/da5a0004b2e1ced774d9","id": 89,"nickname": "豫魏","qrcode": null},"author": "豫魏","content_url": "http://toutiao.com/group/6645831553769275662/","copyright_stat": 11,"cover": "http://p9-tt.bytecdn.cn/list/300x196/113e70006ef2d631e1403.webp","digest": "人活着累的原因是心里装的事情太多，过于功利，想要得到和追求的东西太多。很多时候看到身边的人，总不自觉的把一切和自己对比，总以为别人很顺利，自己总是会有这样那的磨难，心中不免会焦燥烦闷。家家都有本难念的经，谁的日子都不是事事顺意，你没有经历过别人的生活，怎会知道别人心中的苦楚。","id": 10723,"md5_url": "ec07384017a011e9adc9005056c00002","published_at": "2019-01-14","title": "人怎样活才不累？怎样才会幸福？","top": 0},{"account": {"avatar": "http://p3.pstatp.com/thumb/fe3b000017f6bd3b296f","id": 89,"nickname": "阳光中的四叶儿草","qrcode": null},"author": "阳光中的四叶儿草","content_url": "http://toutiao.com/group/6645876128663732743/","copyright_stat": 11,"cover": "http://p9-tt.bytecdn.cn/list/300x196/pgc-image/f3022e15631c41498d6abda607f48669.webp","digest": "铺一纸素笺，用深情的笔，描摹红尘中最美的缘分。思念的长堤，斑斓着玫瑰花的瑰丽，散落了一地花语，那花语凝聚了无限的深情与执念，丝丝缕缕都是为你！","id": 10723,"md5_url": "ea839fd217a011e9b451005056c00002","published_at": "2019-01-14","title": "亲爱的，我爱你！厚重的执念里，一世长情只为你！","top": 0},{"account": {"avatar": "http://p3.pstatp.com/thumb/436400029e60ccc2d6f1","id": 89,"nickname": "壮图山人","qrcode": null},"author": "壮图山人","content_url": "http://toutiao.com/group/6645865517208830472/","copyright_stat": 11,"cover": "http://p9-tt.bytecdn.cn/list/300x196/pgc-image/e4eabcfa7b1348e9b7f29451a628b825.webp","digest": "七律二首·过腊八一一和杨二先生暨东张东望君之一寒侵小院槿篱风，雪尽苍苔瘦井桐。已到年关人迹淡，才闻瓮里酒香隆。","id": 10723,"md5_url": "e5a5371217a011e9be95005056c00002","published_at": "2019-01-14","title": "七律二首/过腊八：年关未做归家梦，更觉乡情逐日稠","top": 0},{"account": {"avatar": "http://p3.pstatp.com/thumb/da8d000a67193c8eca8c","id": 89,"nickname": "21拉克的爱情","qrcode": null},"author": "21拉克的爱情","content_url": "http://toutiao.com/group/6645925261269270797/","copyright_stat": 11,"cover": "http://p3-tt.bytecdn.cn/list/300x196/113e40006f99f0f1a7330.webp","digest": "有极少的伴侣分手多年后选择复合，他们彼此忘不了对方。分手也是因为某种原因，让他们很无奈，但是分手并不是他们的本意。而分手后，他们的心再也装不下别人，那个位置一直为对方保留着。因为他们是真爱，分手或许是为了让对方过的更幸福。","id": 10723,"md5_url": "e2e34d9c17a011e9b083005056c00002","published_at": "2019-01-14","title": "分手多年后能复合吗？","top": 0},{"account": {"avatar": "http://p1.pstatp.com/thumb/b7210002c8e715a90d57","id": 89,"nickname": "感悟你我人生","qrcode": null},"author": "感悟你我人生","content_url": "http://toutiao.com/group/6645975144680391172/","copyright_stat": 11,"cover": "http://p1-tt.bytecdn.cn/list/300x196/pgc-image/0b64ec9dbb8849c4af42938c6d61bd79.webp","digest": "争及湖亭今日会，莫向隙窗笼夜月似说边情向塞云，水阁无尘午昼长草堂潇潇淅江头。高宴华堂夜向阑客心倍伤边候早，正是胡尘欲灭时西风满面吹华发，问白发如何回避头白乘驴悬布囊。","id": 10723,"md5_url": "dc53fa3617a011e9a685005056c00002","published_at": "2019-01-14","title": "哪位老人编的健康长寿顺口溜，太有才了！（句句真理）","top": 0},{"account": {"avatar": "http://p3.pstatp.com/thumb/a14600032b497908673c","id": 89,"nickname": "遇上心语","qrcode": null},"author": "遇上心语","content_url": "http://toutiao.com/group/6645989688576311822/","copyright_stat": 11,"cover": "http://p9-tt.bytecdn.cn/list/300x196/dfic-imagehandler/53fc1ccc-9a2b-4138-8cfc-4c7ba838fd21.webp","digest": "不懂珍惜，守着金山也不会快乐;不懂宽容，再多的朋友也终将离去;不懂选择，再努力也难以成功;不懂行动，再聪明也难以圆梦;不懂合作，再拼搏也难以大成;不懂积累，再挣钱也难以大富;不懂满足，再富有也难以幸福;不懂养生，再治疗也难以长寿。","id": 10723,"md5_url": "d9f7159a17a011e9b76a005056c00002","published_at": "2019-01-14","title": "1月14日（微笑那是我们伸向，另一个人内心最短的道路）周一早安","top": 0},{"account": {"avatar": "http://p3.pstatp.com/thumb/dad5000743a682ba2f66","id": 89,"nickname": "卿城笑","qrcode": null},"author": "卿城笑","content_url": "http://toutiao.com/group/6645808181723267336/","copyright_stat": 11,"cover": "http://p1-tt.bytecdn.cn/list/300x196/113f30006ef49c36f0916.webp","digest": "有的时候也得认命，因为生活中有些难以改变的事情，比如出生和父母，你必须接受，适应它，善待它。我们寄托于命运大多是缘于苦难而没有改变的方法，过去的事情无法再来一次。但是，又不能认命，因为不甘于现状，有自己更高更好的向往追求。","id": 10723,"md5_url": "d83f25f817a011e9b165005056c00002","published_at": "2019-01-14","title": "你们相信命吗？","top": 0}],"msg": "success","page": 5,"size": 10}
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
	'''查询类目文档
		tags:
		- Articles API
		  200:
			description: 返回新闻类目信息
			examples:
			data :{ "cate_list": [{"cate_id": 1,"cate_name": "搞笑"},{"cate_id": 2,"cate_name": "科技"},{"cate_id": 3,"cate_name": "励志"} ],"code": 200}
	'''
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
		tags:
		  - Articles API
		parameters:
		  - name: uuid
			in: path
			type: string
			enum: 1
			required: true
			default: 1
			description: 数据起页坐标
		responses:
		  200:
			description: 返回新闻数据信息
			examples:
            data: {"cate": "科技","grad_read_count": 55,"nes_content": "<img src=\"http://p9-tt.bytecdn.cn/large/pgc-image/RF55DkY6T4YqJp\"><p>2019年1月14日亿欧独家消息，即食水产消费品公司——不等食品近期获千万元级A轮融资，本轮由险峰长青领投，迭代资本跟投。早在去年8月，不等食品获迭代资本750万元Pre-A轮融资。</p><p>不等食品创始人张岳告诉亿欧，本轮资金将用于进一步升级原浆工厂，加强口味的研发；推动线下零售渠道布局，以及扩大全年度产品的销售占比。预计2019年，全年度产品的数量超过50%，销售额超过70%。而此前，不等食品主要通过季节性产品切入市场，其中一款全网明星商品“满满蟹粉”，月销售数量稳定在线上3万罐左右。</p><p>2014年不等食品创立，与国内一流的高级餐厅/名厨合作，把餐厅招牌菜，批量制作为3R系列（ready to eat、ready to heat、ready to cook）的快消即食水产。其中通过对核心调味环节原浆的控制，1：1还原菜品本味，提高高级餐厅/名厨的量产能力，打造全网爆款。目前，白兰地熟醉小龙虾、手作花雕熟醉蟹、满满蟹粉三款单品已成为不等食品的代表产品。</p><p>亿欧曾采访过张岳，短短不到半年时间，不等食品再获融资，不难看出资本对其青睐。张岳介绍，近半年，不等食品主要围绕以下几个方面开展工作：</p><p>1、完成了上海和浙江区域的线下渠道布局，进驻了盒马、超级物种等渠道，同时也正在储备现代零售渠道资源，准备进一步入驻商超、便利店等。</p><p>2、加大对零嘴海鲜产品的投入开发，目前已完成了8款全年度海鲜产品的开发，预计今年3月推向市场。从包装到口味设计，新款产品将采取让消费者更为眼前一亮的体验设计。</p><p>3、确定了基于线上会员的D2C（Direct to Customer）业务模型，沉淀用户。不等食品的线上会员，他们更像是产品的发烧友，与不等一起共建新品。用户通过支付会员费成为会员后，可享受全线商品的优惠折扣；获得进入不等食研院的资格，免费参与新品的测试；在生日和重要节日，还会收到会员专属惊喜礼包。</p><p>张岳预计，今年不等食品在产品端有如下三个发力方向：</p><p>1、重点打造2个系列。把时令型的蟹虾类食品，打造成了时令海鲜系列，进一步强化3R产品开发，推动餐饮零售化；把全年度的海鲜产品，打造成零嘴海鲜系列。</p><p>2、口味进一步改进。口味向江浙以外的地区外延，开发粤菜、川菜、西南菜系等口味。</p><p>3、强化数据系统的搭建，进一步做好用户社群和会员沉淀，壮大不等食研院的规模。预计不等食研院的人数从去年的3000人提升到今年3万人。</p><p>2018年，不等食品还担任了天猫生鲜3R类目的品类舰长，与天猫一起共建3R类目。推动以前只在餐饮端出现的商品，通过液氮极冻、辐照杀菌等最新的食品工艺，进一步把改良商品。天猫3R类目也从去年年初，月度交易额约200-300万，增长到2019年4月可预计突破月交易额1.5亿。不等食品基于自己的实战经验和天猫共享的部分数据，与天猫一起参与共建即食水产类目，推动线上的餐饮零售化。</p><p>不等食品的核心定位是，把各地优秀主厨的手艺和招牌菜系重构为可标准化量产的工业级产品，设计生产年轻用户喜爱的打开就能吃的水产消费品。在品牌定位上，不等食品依然强调走大众化的消费品品牌路线。2019年，在价格和产品带的划分上，不等食品将做进一步下沉。值得一提的是，不等食品在原有3款大粒酱产品的基础上，今年将上线了2款常温的大粒酱（特点是真材实料、颗颗可见），包括鳗鱼牛肉酱、孜然章鱼酱。这类商品的定位，更像是外卖伴侣，对标十元出头的价格区间，为不会做饭的年轻人提供升级的佐餐体验。</p><p>险峰长青副总裁林颖表示，不等团队在产品研发和供应链品质敬畏的初心深深打动了我们，希望不等能将更多中国餐桌上美味的水产菜肴，改造成平价的即食水产品，带给大众消费者。</p><p>迭代资本合伙人周响东表示，过去四十年中国经济快速发展，主流消费人群消费能力提升迅速、消费特征变化很大，同时随着互联网的渗透重构消费场景，这中间会产生很多新品牌的机会。14年初，我在不等食品创业之初就认识团队，看到了团队的成长，以及团队持续的学习能力。通过四年的了解，我非常看好这个团队，相信他们能够取得成功。所以在2018年年初，我们投资了不等食品，本轮我们继续跟投。</p>","t_author": "亿欧网","t_time": "2019-01-14","title": "独家丨不等食品获A轮千万元级融资，打造一流的海鲜快消品牌"}}
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
