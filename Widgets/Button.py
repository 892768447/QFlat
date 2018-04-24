#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QFont, QHelpEvent
from PyQt5.QtWidgets import QPushButton, QStyleOptionButton, QStyle

from Core.Property import Property
from Widgets.ToolTip import ToolTip


# Created on 2018年4月16日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Widgets.Button
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Button(QPushButton, Property):

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.setMinimumHeight(34)

    def event(self, event):
        if isinstance(event, QHelpEvent):
            return False
        return super(Button, self).event(event)

    def enterEvent(self, event):
        """鼠标进入事件"""
        super(Button, self).enterEvent(event)
        if not self.toolTip():
            return
        ToolTip.showText(self, self.toolTip())

    def leaveEvent(self, event):
        """鼠标离开事件"""
        super(Button, self).leaveEvent(event)
        if not self.toolTip():
            return

    def paintEvent(self, event):
        """重绘界面"""
        option = QStyleOptionButton()
        self.initStyleOption(option)
        hover = option.state == (option.state | QStyle.State_MouseOver)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        if not self.isFlat():
            # 绘制背景颜色
            painter.setBrush(
                self.backgroundColorHover if hover else self.backgroundColor)
            # 边框
            painter.setPen(QPen(
                # 如果鼠标按下则边框颜色为背景色(边框效应)
                self.backgroundColor if self.isDown() else (
                    self.borderColorHover if hover else self.borderColor),
                # 鼠标按下则边框宽度 + 5(边框效应)
                self.borderWidth + 5 if self.isDown() else self.borderWidth,
                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            # 绘制区域
            path = QPainterPath()
            path.addRoundedRect(0, 0, self.width(), self.height(),
                                self.borderRadius, self.borderRadius)
            painter.setClipPath(path)
            painter.drawPath(path)
        # 绘制文字
        font = self.font() or QFont()
        font.setUnderline(self.isFlat() and hover)  # 如果是设置的Flat并且鼠标悬停则加上下划线
        painter.setFont(font)
        painter.setPen(self.textColorHover if hover else self.textColor)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())
