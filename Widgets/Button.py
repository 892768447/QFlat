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
    StyleTpl = Template("""/*QFlat Button Style*/
QPushButton {
    width: 90px;
    height: 30px;
    border: {{ _borderWidth }}px solid rgba({{ _borderColor }});
    border-radius: {{ _borderRadius }}px;
    color: rgba({{ _textColor }});
    background-color: rgba({{ _backgroundColor }});
}
QPushButton:hover {
    border: {{ _borderWidth }}px solid rgba({{ _borderColorHover }});
    border-radius: {{ _borderRadius }}px;
    color: rgba({{ _textColorHover }});
    background-color: rgba({{ _backgroundColorHover }});
}
QPushButton:pressed {
    border: {{ _borderWidth + 5 }}px solid rgba({{ _borderColorPressed }});
    border-radius: {{ _borderRadius }}px;
    color: rgba({{ _textColorPressed }});
    background-color: rgba({{ _backgroundColorPressed }});
}
    """)

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

    def update(self):
        self.setStyleSheet(self.generateStyle())
        super(Button, self).update()
