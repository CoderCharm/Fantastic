# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/4/9 14:39
# @Desc: 
"""
用户相关操作
"""
from flask import request

from extensions import Resource, swagger
from api.models.user import FanUser


class AuthUser(Resource):
    def get(self):
        request.get_json("")
        return {'code': 123}

    @swagger.operation(
        notes='some really good notes',
        responseClass="json",
        # method="POST",
        nickname='auth',
        parameters=[
            {
                "name": "account",
                "description": "账号",
                "required": True,
                "allowMultiple": False,
                "value": False,
                "dataType": "str",
                # "paramType": "body"
            },
            {
                "name": "password",
                "description": "密码",
                "required": True,
                "allowMultiple": False,
                "dataType": "str",
                # "paramType": "body"
            }
        ])
    def post(self):
        """
        后台用户登陆
        :return:
        """
        # 获取参数
        try:
            account = request.json.get("account")
            password = request.json.get("password")
        except Exception as e:
            print(e)
            return {"code": 400, "msg": "Invalid input"}

        if not account or not password:
            return {"code": 0, "msg": "Invalid input account and password"}
        # 判断是否有此用户
        user = FanUser.query.filter_by(f_name=account).first()
        if not user:
            return {"code": 0, "msg": "account or password error"}

        if user.verify_password(password):
            # 密码验证正确
            authentication = user.generate_auth_token()  # 认证token
            refresh_token = user.generate_auth_token(expiration=604800)  # 刷新token  # 60*60*24*7
            return {
                "code": 200,
                "Authentication": authentication,
                "RefreshToken": refresh_token,
            }
        else:
            return {
                "code": 0,
                "msg": "account or password error"
            }
