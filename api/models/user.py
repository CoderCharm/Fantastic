#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 10:12
# @Author  : wgPython
# @File    : user.py
# @Software: PyCharm
# @Desc    :
"""
用户模型类
"""
from itsdangerous import SignatureExpired, BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash

from api.models.index import BaseModel
from config import Config
from extensions import db


class FanRole(db.Model, BaseModel):
    """
    后台角色表
    """
    f_role_name = db.Column(db.String(128), nullable=False, comment="角色名称")  # 角色名称 如管理员  普通用户

    def __init__(self, **kwargs):
        super(FanRole, self).__init__(**kwargs)

    @staticmethod
    def create_role():
        for name in ['普通用户', '管理员']:
            role = FanRole(f_role_name=name)
            db.session.add(role)
        db.session.commit()


class FanUser(db.Model, BaseModel):
    """
    用户表
    """
    f_uid = db.Column(db.String(64), nullable=False)  # 用户ID
    f_name = db.Column(db.String(128), nullable=False, comment="用户名")  # 用户名
    f_password = db.Column(db.String(128), nullable=False, comment="密码")  # 密码 MD5
    f_role = db.Column(db.String(8), comment="角色id")  # 用户角色级别 存储角色id
    f_email = db.Column(db.String(64), comment="邮箱")  # 邮箱用于找回密码
    f_phone = db.Column(db.String(8), comment="手机号")

    def __init__(self, **kwargs):
        super(FanUser, self).__init__(**kwargs)

    def hash_password(self, password):  # 创建用户时，生成对应的密码散列值
        self.f_password = generate_password_hash(password)

    def verify_password(self, password):  # 用户登录时，对比用户传输的密码和经过保存的密码hash数值
        return check_password_hash(self.f_password, password)

    def generate_auth_token(self, expiration=7200):
        # 生成认证token   默认过期时间 7200 秒 2*60*60
        s = Serializer(Config.SECRET_KEY, expires_in=expiration)
        return (s.dumps({'f_uid': self.f_uid})).decode('ascii')

    @staticmethod
    def verify_auth_token(token):
        # 验证token
        s = Serializer(Config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return False  # valid token, but expired
        except BadSignature:
            return False  # invalid token
        # user = FanUser.query.get(data['f_uid'])
        return True
