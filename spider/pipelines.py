# import os
# os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import uuid
from app.models import db, FanTaskDetail, FanTask
from sqlalchemy import exc  # 捕获异常


class MysqlPipline(object):
	# Write to mysql using a synchronous mechanism
	
	def process_item(self, item, spider):
		print("-----------A--------------")
		article_list = FanTask(
			t_author=item["t_author"],
			t_author_img=item["t_author_img"],
			uuid=uuid.uuid1().hex,
			t_title=item["t_title"],
			t_desc=item["t_desc"],
			t_image=item["t_image"],
			t_url=item["t_url"],
			t_key=item["t_key"],
			t_cate=item["t_cate"],
			video_second=item["video_second"],
			video_url=item["video_url"],
			tags=item["tags"],
			task_platform=item["task_platform"],
			grad_read_count=item["grad_read_count"],
			grad_forward_count=item["grad_forward_count"],
			grad_comments_count=item["grad_comments_count"],
			article_type=item["article_type"],
			t_author_id=item['t_author_id']
			
		)
		print()
		
		try:
			db.session.add(article_list)
			db.session.commit()
			article_detail = FanTaskDetail(task_id=article_list.task_id, task_content=item["task_content"])
			print(item["task_content"])
			db.session.add(article_detail)
			db.session.commit()
		except exc.SQLAlchemyError:
			print("------------C-----------")
			db.session.rollback()
		print("---------B------------")
		# 返回交给下一个管道文件处理
		return item
