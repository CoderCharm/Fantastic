#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 20:57
# @Author  : wgPython
# @File    : v2_views.py
# @Software: PyCharm
# @Desc    :
"""

"""

from flask import Blueprint
from flask_restful import Api

from api.v2.demo.index import ABC

blueprint = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api_v2 = Api(blueprint)

api_v2.add_resource(ABC, '/abc/test')

