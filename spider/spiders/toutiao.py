# -*- coding: utf-8 -*-
import os
import re
import time
import json
import datetime
import random

import requests

import scrapy
from spider.items import FanTaskItem


class ToutiaoSpider(scrapy.Spider):
    """
    Initialization data
    """

    name = 'toutiao'
    allowed_domains = ['lg.snssdk.com']
    # 抓取的类目
    # Crawled category
    # 搞笑 1 Funny
    a_funny = 'http://lg.snssdk.com/api/news/feed/v88/?list_count=0&support_rn=4&category=funny&concern_id=6215497900768627201&refer=1&refresh_reason=5&session_refresh_idx=1&count=20&last_refresh_sub_entrance_interval=1542699459&loc_mode=7&tt_from=enter_auto&plugin_enable=3&iid=51369582866&device_id=59158791433&ac=wifi&channel=xiaomi&aid=13&app_name=news_article&version_code=698&version_name=6.9.8&device_platform=android&ab_version=494122%2C571131%2C564264%2C239097%2C603059%2C599123%2C170988%2C493250%2C398176%2C602966%2C594603%2C374117%2C437000%2C585118%2C588069%2C594928%2C569578%2C550042%2C572494%2C586993%2C569343%2C602657%2C602521%2C578719%2C584498%2C602510%2C522765%2C602588%2C385748%2C416055%2C592541%2C392485%2C470731%2C604663%2C558139%2C555254%2C378451%2C471406%2C603440%2C596392%2C550819%2C598626%2C602465%2C574603%2C602825%2C603382%2C603400%2C603403%2C603406%2C271178%2C593348%2C594893%2C471797%2C326532%2C586291%2C597115%2C594159%2C604473%2C589799%2C593600%2C591898%2C603984%2C603444%2C604022%2C536966%2C604180%2C554836%2C549647%2C424176%2C31210%2C572465%2C601967%2C603827%2C591175%2C442255%2C604475%2C569779%2C546700%2C280448%2C281296%2C589819%2C594876%2C325612%2C583601%2C578584%2C604014%2C603484%2C594402%2C586524%2C603083%2C603973%2C498375%2C467513%2C602487%2C603139%2C584241%2C604222%2C580448%2C595556%2C600117%2C574249%2C486951%2C599433%2C591650%2C604157%2C475366%2C592286%2C552034%2C589102%2C590514%2C293032%2C457481%2C562442&ab_client=a1%2Cc4%2Ce1%2Cf1%2Cg2%2Cf7&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=Redmi+5+Plus&device_brand=xiaomi&language=zh&os_api=25&os_version=7.1.2&uuid=868027034942221&openudid=624b9b070d7b2634&manifest_version_code=698&resolution=1080*2030&dpi=440&update_version_code=69811&_rticket=1542699459201&fp=G2T_PzGOLzKSFl4ML2U1F2KecMw1&tma_jssdk_version=1.5.3.1&rom_version=miui_v9_v99.9.9.9.negcnfa&plugin=26958&ts=1542699459&as=a2c5cb6fd36c3bd9f34355&mas=0019fc4a23e7659c4117dad0fd02389c5af6a7a2e806686ead&cp=5ab3fc32b29c3q1'
    # 励志 2 Inspirational
    a_essay = 'http://lg.snssdk.com/api/news/feed/v88/?list_count=17&support_rn=4&category=news_essay&concern_id=6215497897899723265&refer=1&refresh_reason=1&session_refresh_idx=2&count=20&min_behot_time=1542699328&last_refresh_sub_entrance_interval=1542699770&loc_mode=7&tt_from=pull&plugin_enable=3&iid=51369582866&device_id=59158791433&ac=wifi&channel=xiaomi&aid=13&app_name=news_article&version_code=698&version_name=6.9.8&device_platform=android&ab_version=494122%2C571131%2C564264%2C239097%2C603059%2C599123%2C170988%2C493250%2C398176%2C602966%2C594603%2C374117%2C437000%2C585118%2C588069%2C594928%2C569578%2C550042%2C572494%2C586993%2C569343%2C602657%2C602521%2C578719%2C584498%2C602510%2C522765%2C602588%2C385748%2C416055%2C592541%2C392485%2C470731%2C604663%2C558139%2C555254%2C378451%2C471406%2C603440%2C596392%2C550819%2C598626%2C602465%2C574603%2C602825%2C603382%2C603400%2C603403%2C603406%2C271178%2C593348%2C594893%2C471797%2C326532%2C586291%2C597115%2C594159%2C604473%2C589799%2C593600%2C591898%2C603984%2C603444%2C604022%2C536966%2C604180%2C554836%2C549647%2C424176%2C31210%2C572465%2C601967%2C603827%2C591175%2C442255%2C604475%2C569779%2C546700%2C280448%2C281296%2C589819%2C594876%2C325612%2C583601%2C578584%2C604014%2C603484%2C594402%2C586524%2C603083%2C603973%2C498375%2C467513%2C602487%2C603139%2C584241%2C604222%2C580448%2C595556%2C600117%2C574249%2C486951%2C599433%2C591650%2C604157%2C475366%2C592286%2C552034%2C589102%2C590514%2C293032%2C457481%2C562442&ab_client=a1%2Cc4%2Ce1%2Cf1%2Cg2%2Cf7&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=Redmi+5+Plus&device_brand=xiaomi&language=zh&os_api=25&os_version=7.1.2&uuid=868027034942221&openudid=624b9b070d7b2634&manifest_version_code=698&resolution=1080*2030&dpi=440&update_version_code=69811&_rticket=1542699770687&fp=G2T_PzGOLzKSFl4ML2U1F2KecMw1&tma_jssdk_version=1.5.3.1&rom_version=miui_v9_v99.9.9.9.negcnfa&plugin=26958&ts=1542699770&as=a245fb2fba3f3bea634355&mas=00dd83e5569d43e884314982efb8257ce6e40c02e806686ee5&cp=51baf536b7afaq1'
    # 科技  3 Technology
    a_technology = 'http://lg.snssdk.com/api/news/feed/v88/?list_count=0&support_rn=4&category=news_tech&concern_id=6215497899594222081&refer=1&refresh_reason=5&session_refresh_idx=1&count=20&last_refresh_sub_entrance_interval=1542698862&loc_mode=7&tt_from=enter_auto&plugin_enable=3&iid=51369582866&device_id=59158791433&ac=wifi&channel=xiaomi&aid=13&app_name=news_article&version_code=698&version_name=6.9.8&device_platform=android&ab_version=536966%2C604180%2C554836%2C549647%2C424176%2C31210%2C572465%2C601967%2C603827%2C591175%2C442255%2C604475%2C569779%2C546700%2C280448%2C281296%2C589819%2C594876%2C325612%2C583601%2C578584%2C604014%2C603484%2C594402%2C586524%2C603083%2C603973%2C498375%2C467513%2C602487%2C603139%2C584241%2C604222%2C580448%2C595556%2C600117%2C574249%2C486951%2C599433%2C591650%2C604157%2C475366%2C494122%2C571131%2C564264%2C239097%2C603059%2C599123%2C170988%2C493250%2C398176%2C602966%2C594603%2C374117%2C437000%2C585118%2C588069%2C594928%2C569578%2C550042%2C572494%2C586993%2C569343%2C602657%2C602521%2C578719%2C584498%2C602510%2C522765%2C602588%2C385748%2C416055%2C592541%2C392485%2C470731%2C558139%2C555254%2C378451%2C471406%2C603440%2C596392%2C550819%2C598626%2C602465%2C574603%2C602825%2C603382%2C603400%2C603403%2C603406%2C271178%2C593348%2C594893%2C471797%2C326532%2C586291%2C597115%2C594159%2C604473%2C589799%2C593600%2C591898%2C603984%2C603444%2C604022%2C562442%2C592286%2C552034%2C589102%2C590514%2C293032%2C457481&ab_client=a1%2Cc4%2Ce1%2Cf1%2Cg2%2Cf7&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=Redmi+5+Plus&device_brand=xiaomi&language=zh&os_api=25&os_version=7.1.2&uuid=868027034942221&openudid=624b9b070d7b2634&manifest_version_code=698&resolution=1080*2030&dpi=440&update_version_code=69811&_rticket=1542698862622&fp=G2T_PzGOLzKSFl4ML2U1F2KecMw1&tma_jssdk_version=1.5.3.1&rom_version=miui_v9_v99.9.9.9.negcnfa&plugin=26958&ts=1542698862&as=a2b58bdf4ef6ab57334355&mas=00eefd724866b9ec63b0d08d5473f0c8732e0a08e806686eb6&cp=5fb2f631b276eq1'

    # toutiao api
    start_urls = [a_funny, a_essay, a_technology]
    custom_settings = {
        "DOWNLOAD_DELAY": random.uniform(5, 10),
        # "LOG_LEVEL": "DEBUG",  # 打印日志等级
        'ITEM_PIPELINES': {
            'spider.pipelines.MysqlPipline': 100,
        },
    }
    site_name = '今日头条爬虫'
    version = '2.0'
    task_platform = 1
    # start_url下角标计数
    num = 0
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        "Host": "lg.snssdk.com",
        "X-SS-REQ-TICKET": int(time.time() * 1000),
    }

    def handle_error(self, failure):
        """
        回调函数 处理错误
        :param failure:
        :return:
        """
        self.logger.error("{}--Spider GG------".format(self.site_name))
        self.logger.error("Error Handle: {}".format(failure.request))
        self.log("Spider GG and  Sleeping 60 seconds")
        time.sleep(60)
        self.num = 0
        self.headers["X-SS-REQ-TICKET"] = int(time.time() * 1000)
        random.shuffle(self.start_urls)

        yield scrapy.Request(
            random.choice(self.start_urls),
            headers=self.headers,
            callback=self.parse,
            errback=self.handle_error,
            dont_filter=True
        )

    def start_requests(self):
        """
        爬虫请求开始
        :return:
        """
        print("{0} Start".format(self.site_name))
        self.headers["X-SS-REQ-TICKET"] = int(time.time() * 1000)

        yield scrapy.Request(
            random.choice(self.start_urls),
            headers=self.headers,
            dont_filter=True,
            errback=self.handle_error,
            callback=self.parse,
        )

    def parse(self, response):
        item = FanTaskItem()
        try:
            item["task_platform"] = self.task_platform
            item["article_type"] = 1
            item["video_url"] = "0"
            item["video_second"] = "0"
            # 根据url后缀判断分类
            # According to the url suffix judgment classification
            re_url = response.url
            if re_url == self.a_funny:
                item["t_cate"] = 1  # 搞笑
            elif re_url == self.a_technology:
                item["t_cate"] = 2  # 科技
            elif re_url == self.a_essay:
                item["t_cate"] = 3  # 励志
    
            json_data = json.loads(response.text)
            info_list = json_data.get("data", list())
            for detail_data in info_list:
                new_content = json.loads(detail_data["content"])
                item["t_title"] = new_content.get("title")  # 标题
                item['t_author'] = new_content.get("media_name")  # 作者
                # 作者头像
                item['t_author_img'] = new_content.get('user_info')['avatar_url']
        
                article_id = new_content.get("item_id")  # id
                item["t_key"] = "toutiao" + str(article_id)
                # '''数据去重'''
                # 这里需要数据去重 我在这里没有做
                # I need data to be heavy here. I have not done it here.
                item['tags'] = ''
                item["t_desc"] = new_content.get("abstract")  # 简介
                if not item["t_desc"]:  # 如果简介为空　　就等于标题  If the profile is empty, it is equal to the title
                    item["t_desc"] = item["t_title"]
                if len(str(item["t_desc"])) < 5:
                    # 防止有些简介是空字符串直接赋值标题 Prevent some profiles from being empty strings directly assigning headers
                    item["t_desc"] = item["t_title"]
                # 阅读 read num
                item["grad_read_count"] = new_content.get("read_count", "0")
                # 评论 comment num
                item["grad_comments_count"] = new_content.get("comment_count", "0")
                # 转发  Forward num
                item["grad_forward_count"] = new_content.get("share_count", "0")
                item["t_url"] = new_content.get("display_url", "")
                # 去除一些不合理的内容比如悟空问答  Remove some unreasonable content such as Goku Q & A
                if "wukong.com" in item["t_url"]:
                    print("悟空问答去掉---{}__{}".format(item["t_title"], article_id))
                    continue
                if "toutiao.com/group" not in item["t_url"]:
                    print("数据不合法......{}__{}__{}".format(item["t_url"], item["t_title"], article_id))
                    continue
                # 只获取一张图片 如果获取三张把[0]['url'] 去掉  Get only one picture. If you get three, remove [0]['url']
                t_image = new_content.get("image_list", list())
                if t_image:
                    item["t_image"] = t_image[0]['url']
                else:
                    # 没有就取一张图的
                    middle_image = new_content.get("middle_image", list())
                    if middle_image:
                        item["t_image"] = new_content.get("middle_image", list())['url']
                    else:
                        item["t_image"] = new_content.get("middle_image", list())
                # 首图不能为空  The first picture cannot be empty
                if item["t_image"]:
                    time.sleep(random.uniform(2, 5))  # 随机2-5秒 Random 2-5 seconds
                    detail_info = requests.get(
                        'http://a3.pstatp.com/article/content/21/1/{}/{}/1/0/?iid=37457543399&device_id=55215909025&ac=wifi&channel=tengxun2&aid=13&app_name=news_article&version_code=682&version_name=6.8.2&device_platform=android&ab_version=261581%2C403271%2C197606%2C293032%2C405731%2C418881%2C413287%2C271178%2C357705%2C377637%2C326524%2C326532%2C405403%2C415915%2C409847%2C416819%2C402597%2C369470%2C239096%2C170988%2C416198%2C390549%2C404717%2C374117%2C416708%2C416648%2C265169%2C415090%2C330633%2C297058%2C410260%2C276203%2C413705%2C320832%2C397738%2C381405%2C416055%2C416153%2C401106%2C392484%2C385726%2C376443%2C378451%2C401138%2C392717%2C323233%2C401589%2C391817%2C346557%2C415482%2C414664%2C406427%2C411774%2C345191%2C417119%2C377633%2C413565%2C414156%2C214069%2C31211%2C414225%2C411334%2C415564%2C388526%2C280449%2C281297%2C325614%2C324092%2C357402%2C414393%2C386890%2C411663%2C361348%2C406418%2C252782%2C376993%2C418024&ab_client=a1%2Cc4%2Ce1%2Cf1%2Cg2%2Cf7&ab_feature=102749%2C94563&abflag=3&ssmix=a&device_type=MI+3C&device_brand=Xiaomi&language=zh&os_api=19&os_version=4.4.4&uuid=99000549116036&openudid=efcc6d4284c6c458&manifest_version_code=682&resolution=1080*1920&dpi=480&update_version_code=68210&_rticket=1532142082952&rom_version=miui_v7_5.12.4&plugin=32&pos=5r_88Pzt0fzp9Ono-fi_p66ps6-oraylqrG__PD87d706eS_p794Iw14KgN4JR-_sb_88Pzt0fLz-vTp6Pn4v6esrKqzrKSvqq6k4A%3D%3D&fp=z2T_L2mOLSxbFlHIPlU1FYweFzKe&ts=1532142082&as=a255cac5b2208bd2a23862&mas=00e35bc961329fe4e2da0242394f32b692264a2c00d8a582a8'.format(
                            article_id, article_id),
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
                            "Host": "a3.pstatp.com",
                            "X-SS-TC": "0",
                        },
                        timeout=30, verify=False
                    )
                    html = json.loads(detail_info.text)
                    # 获取图片的url Get the url of the image
                    src_lists = html['data']['image_detail']
                    a_url = []
                    for src in src_lists:
                        src_url = src['url']
                        a_url.append(src_url)
            
                    # 内容抓取  Content crawling
                    content = html['data']['content']
                    # 内容处理
                    pat = re.compile(r'</header>(.*?)<footer></footer>', re.S)
                    news_content = pat.findall(content)[0].replace('type="gif"', '')
                    # 匹配所有的img
                    pat = re.compile(r'<a class="image"  href=(.*?)></a>', re.S)
                    content_img = pat.findall(news_content)
                    if content_img:
                        for i in range(len(content_img)):
                            if content_img[i] in news_content:
                                news_content = news_content.replace(content_img[i], a_url[i]).replace(
                                    '<a class="image"  href=',
                                    '<img src="').replace('></a>',
                                                          '">')
                    if '<p class="footnote">' in news_content:
                        # 进行匹配,去除名字
                        pat = re.compile(r'<p class="footnote">(.*?)</p>', re.S)
                        names_1 = pat.findall(news_content)[0]
                        news_content = news_content.replace('<p class="footnote">' + names_1 + '</p>', '')
                    catch_img_list = []
                    # 图片下载
                    for url in a_url:
                        src = {}
                        # 把url进行切割
                        fname = url.split('/')[-1][10:]
                        # 生成当天时间
                        times = str(datetime.date.today()).replace('-', '/')
                        # 现在时间
                        date_time = str(datetime.datetime.now()).replace('-', '').replace(' ', '').replace(':', '')[:14]
                        # 图片的路径
                        src_img = '/contentpic/' + times + '/' + date_time + '_' + fname
                        # 判断有没有这个文件
                        if not os.path.exists('/contentpic/' + times):
                            os.makedirs('/contentpic/' + times)
                        # try:
                        #     request.urlretrieve(url, src_img)
                        # # putoss(src_img)
                        # except Exception as e:
                        #     request.urlretrieve(url, src_img)
                        # # putoss(src_img)
                        # 图片路径
                        src['src'] = src_img
                
                        catch_img_list.append(src)
                        # if url in news_content:
                        #     #         # 进行替换
                        #     #         # 进行替换
                        #     news_content = news_content.replace(url, 'http://katu.haocishop.cn' + src_img)
                        # if url in news_content:
                        # 	#         # 进行替换
                        # 	news_content = news_content.replace(url, 'http://katu.haocishop.cn' + src_img)
                        # 正则 只保留 p img 标签  Regular only keep p img tags
                        # print(news_content)
                        news_content = re.sub(r"<(?!/?\s?p|/?\s?img)[^<>]*>", "", news_content)
                        news_content = re.sub(r"<p[\S\s]*?>", "<p>", news_content)
                        news_content = news_content.replace('\n', '')
                        item['task_content'] = news_content
                
                        yield item
        except:
            print('问题数据：')

        print("休眠请求下一页Url....")
        time.sleep(random.uniform(5, 15))
        self.num += 1
        if self.num >= len(self.start_urls):
            self.num = 0
            random.shuffle(self.start_urls)
            time.sleep(random.uniform(20, 30))
        self.headers["X-SS-REQ-TICKET"] = int(time.time() * 1000)
        yield scrapy.Request(
            self.start_urls[self.num],
            headers=self.headers,
            dont_filter=True,
            errback=self.handle_error,
            callback=self.parse,
        )
