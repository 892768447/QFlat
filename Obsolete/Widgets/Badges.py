#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年9月13日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.Badges
@description: 
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QFont
from PyQt5.QtWidgets import QLabel

from Core.Property import Property


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class Badges(QLabel, Property):

    def __init__(self, *args, **kwargs):
        super(Badges, self).__init__(*args, **kwargs)

    def resizeEvent(self, event):
        self.borderRadius = min(self.width(), self.height()) / 2
        super(Badges, self).resizeEvent(event)

    def paintEvent(self, event):
        """重绘界面"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # 绘制背景颜色
        painter.setBrush(self.backgroundColor)
        # 边框
        painter.setPen(QPen(self.borderColor, self.borderWidth,
                            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        # 绘制区域
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(),
                            self.borderRadius, self.borderRadius)
        painter.setClipPath(path)
        painter.drawPath(path)
        # 绘制文字
        font = self.font() or QFont()
        painter.setFont(font)
        painter.setPen(self.textColor)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())
