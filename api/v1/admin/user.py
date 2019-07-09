# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/4/9 14:39
# @Desc: 
"""
用户相关操作
"""
from flask import request, make_response
from extensions import Resource
from flask_wtf.csrf import generate_csrf


class Login(Resource):

    @staticmethod
    def get():
        csrf_token = generate_csrf()
        res = make_response().set_cookie("csrf_token", csrf_token, expires=5000)
        return res, 301

    def post(self):
        """
        后台用户登陆
        :return:
        """
        # 获取参数
        account = request.json.get("account")
        password = request.json.get("password")

        if not account or not password:
            return {"code": 0, "msg": "用户名或密码错误"}

        # 判断是否有此用户

        return {
            "code": 200,
            "login-token": "aaaa",
            "login-cookie": "has been login",
            "account": account,
            "password": password,
        }
