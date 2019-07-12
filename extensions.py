# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2018/12/24 10:32
# @Desc:
"""
extensions file
"""
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Resource
from flask_restful_swagger import swagger

__all__ = ['db', 'CORS', 'Resource', 'swagger']
db = SQLAlchemy()
