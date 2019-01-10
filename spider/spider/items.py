# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass


class FanTaskItem(scrapy.Item):
	"""Article list"""
	t_author = scrapy.Field()  # Original author
	t_author_img = scrapy.Field()  # Author avatar link
	t_title = scrapy.Field()  # title 3
	t_desc = scrapy.Field()  # Introduction
	t_url = scrapy.Field()  # Original link
	t_key = scrapy.Field()  # Unique key crawl article source key
	article_type = scrapy.Field()  # 1: normal type 2: video type
	video_second = scrapy.Field()  # Play time, seconds
	video_url = scrapy.Field()  # Video address
	tags = scrapy.Field()  # Article label
	task_platform = scrapy.Field()  # Article Source
	grad_read_count = scrapy.Field()  # Grab reading
	grad_forward_count = scrapy.Field()  # Crawl forwarding number
	grad_comments_count = scrapy.Field()  # Number of comments fetched
	cate_id = scrapy.Field()  # 分类
	t_image = scrapy.Field()  # 首图
	task_content = scrapy.Field()  # 文章内容
