import pymysql
import time
import requests
import re

# from settings import DATA_BASE

DATA_BASE = {
	"user": "bingbing",
	"password": "123456",
	"host": "39.105.119.228",
	"data_name": "fantastic",
}


class MysqlPipline(object):
	# 采用同步的机制写入mysql Write to mysql using a synchronous mechanism
	def __init__(self):
		try:
			self.conn = pymysql.connect('39.105.119.228', 'bingbing', "123456", "fantastic", charset='utf8')
			# 获取游标对象
			self.cursor = self.conn.cursor()
		except Exception as e:
			print("数据库连接异常", e)
	
	def _reConnect(self):
		"""
		因为总是跑一段时间就会出错　pymysql.err.InterfaceError: (0, '')
		所以这边加一个测试链接ping 来解决此问题  如果ping不通 则重新链接
		
Because it always runs for a while, it will go wrong pymysql.err.InterfaceError: (0, '')
So here is a test link ping to solve this problem. If the ping fails, relink.
		:return:
		"""
		try:
			self.conn.ping()  # 先ping以下链接是否还有效　　
		except:
			# 无效则从新链接
			self.conn = pymysql.connect('39.105.119.228', 'bingbing', "123456", "fantastic", charset='utf8')
			# 获取游标对象
			self.cursor = self.conn.cursor()
	
	def process_item(self, item, spider):
		print("-----------A-------------------")
		sql = 'insert into fan_task(t_author,t_author_img,t_title,t_desc,t_url,t_key,article_type,video_second,video_url,tags,task_platform,grad_read_count,grad_forward_count,grad_comments_count,cate_id,t_image,task_content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
		try:
			self.cursor.execute(sql, (
				item['t_author'], item['t_author_img'], item['t_title'], item['t_desc'], item['t_url'], item['t_key'],
				item['article_type'], item['video_second'], item['video_url'], item['tags'], item['task_platform'],
				item['grad_read_count'], item['grad_forward_count'], item['grad_comments_count'], item['cate_id'],
				item['t_image'], item['task_content']))
			self.conn.commit()
		except Exception as e:
			self.conn.rollback()
			print(e)
			print('执行语句失败')
		# 返回交给下一个管道文件处理
		return item
