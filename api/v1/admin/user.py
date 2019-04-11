# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/4/9 14:39
# @Desc: 
"""
用户相关操作
"""
from flask import request
from flask_restful import Resource


class Login(Resource):
    def get(self):
        return {"aaa": "123"}

    def post(self):
        """
        后台用户登陆
        :return:
        """
        # 获取参数
        account = request.values.get("account")
        password = request.values.get("password")

        if not account or not password:
            return {"code": 0, "msg": "用户名或密码错误"}

        return {
            "code": 200,
            "login-token": "aaaa",
            "login-cookie": "has been login",
            "account": account,
            "password": password,
        }