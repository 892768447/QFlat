#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


# Created on 2018年4月24日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Widgets.ToolTip
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class ToolTip(QLabel):

    Left, Top, Right, Bottom = range(4)
    _instance = None

    def __init__(self, *args, **kwargs):
        super(ToolTip, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.ToolTip | Qt.BypassGraphicsProxyWidget)

    @classmethod
    def showText(self, widget, text='', direction=2):
        """显示文字"""
        if not ToolTip._instance:
            ToolTip._instance = ToolTip()
        ToolTip._instance.setText(text)
        pos = widget.mapToGlobal(widget.pos()) - widget.pos()
        ToolTip._instance.move(pos)
        ToolTip._instance.show()
