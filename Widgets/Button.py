#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年4月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.Button
@description: 
"""


from PyQt5.QtWidgets import QPushButton

from Core.Property import Property
from Core.Template import Template


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0

class Button(QPushButton, Property):
    
    # 样式模版
    StyleTpl = Template("""
    QPushButton {
        border: {{ borderWidth }}px solid {{ borderColor}};
        border-radius: {{ borderRadius }}px;
        color: {{ textColor }};
        background-color: {{ backgroundColor }};
    }
    QPushButton:hover {
        border: {{ borderWidthHover }}px solid {{ borderColorHover }};
        border-radius: {{ borderRadiusHover }}px;
        color: {{ textColorHover }};
        background-color: {{ backgroundColorHover }};
    }
    QPushButton:pressed {
        border: {{ borderWidthPressed }}px solid {{ borderColorPressed }};
        border-radius: {{ borderRadiusPressed }}px;
        color: {{ textColorPressed }};
        background-color: {{ backgroundColorPressed }};
    }
    """)

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

    def update(self):
        print(self.styleSheet())
        super(Button, self).update()
