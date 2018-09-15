#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年4月24日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.ToolTip
@description: 
"""

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QLabel


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
    def showText(self, widget, text='', direction=1):
        '''
        # 显示文字
        :param widget: 要显示文字提示的控件
        :param text: 文字
        :param direction: 方向 ( 左上右下 = 0, 1, 2, 3 )
        '''
        if not ToolTip._instance:
            ToolTip._instance = ToolTip()
        # 设置文本内容
        ToolTip._instance.setText(text)
        # 得到坐标地址
        pos = widget.mapToGlobal(widget.pos()) - widget.pos()
        if direction == self.Left:
            pass
        elif direction == self.Top:
            pos = pos + QPoint(int((widget.width() - ToolTip._instance.width()) / 2),
                               - ToolTip._instance.height() - 10)
        elif direction == self.Right:
            pass
        else:
            pass
        ToolTip._instance.move(pos)
        ToolTip._instance.show()
