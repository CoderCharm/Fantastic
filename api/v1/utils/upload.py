# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/4/11 16:33
# @Desc: 
"""
处理图片上传存储
"""
import time

import os
from flask import request
from extensions import Resource


class UpLoad(Resource):
    def post(self):
        """
        上传图片处理 额  自定义的实际的话一般都会用云存储吧!
        :return:
        """
        # 文件夹名称 通过当前时间

        current_dir = time.strftime("%Y%m%d", time.localtime())
        if not os.path.exists(f"./api/static/{current_dir}"):
            os.mkdir(f"./api/static/{current_dir}")

        res = request.files["wangEditorH5File"]
        file_name = str(int(time.time() * 1000)) + str(res.filename)

        with open(f"./api/static/{current_dir}/{file_name}", "wb") as f:
            f.write(res.read())

        return {"data": [f"http://127.0.0.1:8000/static/{current_dir}/{file_name}"]}
