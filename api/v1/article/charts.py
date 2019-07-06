# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/4/16 10:10
# @Desc: 
"""
数据统计接口
"""
from extensions import Resource


class ChartsCate(Resource):
    def get(self):
        """
        统计每日抓取的各分类数量
        :return:
        """
        return {
            "code": 200,
            "data": {
                "title": {
                    "text": '今日头条每日抓取数据分类',
                    "subtext": '文章',
                    "x": "center",
                },
                "series": {
                    "name": '今日头条',
                    "data": [
                        {"value": 335, "name": '搞笑'},
                        {"value": 310, "name": '励志'},
                        {"value": 234, "name": '养生'},
                        {"value": 435, "name": '娱乐'},
                        {"value": 358, "name": '美食'},
                    ],
                },
                "dataList": ['搞笑', '励志', '养生', '娱乐', '美食'],
            }
        }
