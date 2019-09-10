#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 20:57
# @Author  : wgPython
# @File    : index.py
# @Software: PyCharm
# @Desc    :
"""

"""


from extensions import Resource


class ABC(Resource):

    def get(self):
        return {"hello": "v2"}

