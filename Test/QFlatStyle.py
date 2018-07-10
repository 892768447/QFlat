#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年7月10日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Test.QFlatStyle
@description: 
"""
from PyQt5.QtWidgets import QProxyStyle


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class QFlatStyle(QProxyStyle):

    def __init__(self):
        super(QFlatStyle, self).__init__('fusion')
