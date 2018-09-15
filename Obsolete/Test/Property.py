#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年4月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Core.Property
@description: 属性类
"""

from PyQt5.QtCore import pyqtSignal, pyqtProperty
from PyQt5.QtGui import QColor

from Core.Colors import getColor, White, _Color


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Property:

    White, BlueJeans, Aqua, Mint, Grass, Sunflower, Bittersweet, \
        Grapefruit, Lavender, PinkRose, LightGray, MediumGray, \
        DarkGray = range(13)

    backgroundColorChanged = pyqtSignal(QColor, QColor)  # 背景颜色改变信号
    backgroundColorHoverChanged = pyqtSignal(QColor, QColor)  # 悬停背景颜色改变信号
    borderColorChanged = pyqtSignal(QColor, QColor)  # 边框颜色改变信号
    borderColorHoverChanged = pyqtSignal(QColor, QColor)  # 悬停边框颜色改变信号
    textColorChanged = pyqtSignal(QColor, QColor)  # 文字颜色改变信号
    textColorHoverChanged = pyqtSignal(QColor, QColor)  # 悬停文字颜色改变信号
    borderWidthChanged = pyqtSignal(int, int)  # 边框宽度改变信号
    borderRadiusChanged = pyqtSignal(float, float)  # 边框圆角改变信号

    def __init__(self, *args, **kwargs):
        super(Property, self).__init__(*args, **kwargs)
        self.Color = White()
        self._Color = White()  # 还原色
        self._borderWidth = 0  # 默认边框宽度
        self._borderRadius = 4  # 默认圆角半径

    def setColor(self, color):
        if isinstance(color, _Color):
            self.Color = color
            default, lighter = color.backgroundColors()
            defaultT, lighterT = color.textColors()
            self._Color = _Color(default, lighter)
            self._Color.TextColor = defaultT
            self._Color.TextColorHover = lighterT
        else:
            self.Color = getColor(color)
            self._Color

    def getColor(self):
        return self.Color

##########################################################################

    def resetBackgroundColor(self):
        """* 重置背景颜色"""
        self.backgroundColorChanged.emit(  # 发送信号
            self.Color.BackgroundColor, self._Color.BackgroundColor)
        self.Color.BackgroundColor = self._Color.BackgroundColor
        self.update()

    @pyqtProperty(QColor, freset=resetBackgroundColor, notify=backgroundColorChanged)
    def backgroundColor(self) -> QColor:
        """* 获取背景颜色::
            print(obj.backgroundColor)

        * 设置背景颜色::
            obj.backgroundColor = 'red'
            obj.backgroundColor = '#ff00ff'
            obj.backgroundColor = QColor()
            obj.backgroundColor = 100
            obj.backgroundColor = (255, 255, 255)
            obj.backgroundColor = [255, 255, 255, 255]

        * QSS方式修改::
            obj.setStyleSheet('qproperty-backgroundColor: red;')

        * 当值变化时 `backgroundColorChanged` 信号会被发送
        """
        return self.Color.BackgroundColor

    @backgroundColor.setter
    def backgroundColor(self, color: [str, int, tuple, list]):
        self.Color.BackgroundColor, color = getColor(
            color), self.Color.BackgroundColor
        self.backgroundColorChanged.emit(color, self.Color.BackgroundColor)
        self.update()

##########################################################################

    def resetBackgroundColorHover(self):
        """* 重置悬停背景颜色"""
        self.backgroundColorHoverChanged.emit(  # 发送信号
            self.Color.BackgroundColorHover, self._Color.BackgroundColorHover)
        self.Color.BackgroundColorHover = self._Color.BackgroundColorHover
        self.update()

    @pyqtProperty(QColor, freset=resetBackgroundColorHover, notify=backgroundColorHoverChanged)
    def backgroundColorHover(self) -> QColor:
        """* 获取悬停背景颜色::
            print(obj.backgroundColorHover)

        * 设置悬停背景颜色::
            obj.backgroundColorHover = 'red'
            obj.backgroundColorHover = '#ff00ff'
            obj.backgroundColorHover = QColor()
            obj.backgroundColorHover = 100
            obj.backgroundColorHover = (255, 255, 255)
            obj.backgroundColorHover = [255, 255, 255, 255]

        * QSS方式修改::
            obj.setStyleSheet('qproperty-backgroundColorHover: red;')

        * 当值变化时 `backgroundColorHoverChanged` 信号会被发送
        """
        return self.Color.BackgroundColorHover

    @backgroundColorHover.setter
    def backgroundColorHover(self, color: [str, int, tuple, list]):
        self.Color.BackgroundColorHover, color = getColor(
            color), self.Color.BackgroundColorHover
        self.backgroundColorHoverChanged.emit(
            color, self.Color.BackgroundColorHover)
        self.update()

##########################################################################

    def resetBorderColor(self):
        """* 重置边框颜色"""
        self.borderColorChanged.emit(  # 发送信号
            self.Color.BorderColor, self._Color.BorderColor)
        self.Color.BorderColor = self._Color.BorderColor
        self.update()

    @pyqtProperty(QColor, freset=resetBorderColor, notify=borderColorChanged)
    def borderColor(self) -> QColor:
        """* 获取边框颜色::
            print(obj.borderColor)

        * 设置边框颜色::
            obj.borderColor = 'red'
            obj.borderColor = '#ff00ff'
            obj.borderColor = QColor()
            obj.borderColor = 100
            obj.borderColor = (255, 255, 255)
            obj.borderColor = [255, 255, 255, 255]

        * QSS方式修改::
            obj.setStyleSheet('qproperty-borderColor: red;')

        * 当值变化时 `borderColorChanged` 信号会被发送
        """
        return self.Color.BorderColor

    @borderColor.setter
    def borderColor(self, color: [str, int, tuple, list]):
        self.Color.BorderColor, color = getColor(color), self.Color.BorderColor
        self.borderColorChanged.emit(color, self.Color.BorderColor)
        self.update()

##########################################################################

    def resetBorderColorHover(self):
        """* 重置悬停边框颜色"""
        self.borderColorHoverChanged.emit(  # 发送信号
            self.Color.BorderColorHover, self._Color.BorderColorHover)
        self.Color.BorderColorHover = self._Color.BorderColorHover
        self.update()

    @pyqtProperty(QColor, freset=resetBorderColorHover, notify=borderColorHoverChanged)
    def borderColorHover(self) -> QColor:
        """* 获取悬停边框颜色::
            print(obj.borderColorHover)

        * 设置边框颜色::
            obj.borderColorHover = 'red'
            obj.borderColorHover = '#ff00ff'
            obj.borderColorHover = QColor()
            obj.borderColorHover = 100
            obj.borderColorHover = (255, 255, 255)
            obj.borderColorHover = [255, 255, 255, 255]

        * QSS方式修改::
            obj.setStyleSheet('qproperty-borderColorHover: red;')

        * 当值变化时 `borderColorHoverChanged` 信号会被发送
        """
        return self.Color.BorderColor

    @borderColorHover.setter
    def borderColorHover(self, color: [str, int, tuple, list]):
        self.Color.BorderColorHover, color = getColor(
            color), self.Color.BorderColorHover
        self.borderColorHoverChanged.emit(color, self.Color.BorderColorHover)
        self.update()

##########################################################################

    def resetTextColor(self):
        """* 重置文字颜色"""
        self.textColorChanged.emit(  # 发送信号
            self.Color.TextColor, self._Color.TextColor)
        self.Color.TextColor = self._Color.TextColor
        self.update()

    @pyqtProperty(QColor, freset=resetBorderColor, notify=textColorChanged)
    def textColor(self) -> QColor:
        """* 获取文字颜色::
            print(obj.textColor)

        * 设置文字框颜色::
            obj.textColor = 'red'
            obj.textColor = '#ff00ff'
            obj.textColor = QColor()
            obj.textColor = 100
            obj.textColor = (255, 255, 255)
            obj.textColor = [255, 255, 255, 255]

        * QSS方式修改::
            obj.setStyleSheet('qproperty-textColor: red;')

        * 当值变化时 `textColorChanged` 信号会被发送
        """
        return self.Color.TextColor

    @textColor.setter
    def textColor(self, color: [str, int, tuple, list]):
        self.Color.TextColor, color = getColor(color), self.Color.TextColor
        self.textColorChanged.emit(color, self.Color.TextColor)
        self.update()

##########################################################################

    def resetTextColorHover(self):
        """* 重置悬停文字颜色"""
        self.textColorHoverChanged.emit(  # 发送信号
            self.Color.TextColorHover, self._Color.TextColorHover)
        self.Color.TextColorHover = self._Color.TextColorHover
        self.update()

    @pyqtProperty(QColor, freset=resetTextColorHover, notify=textColorHoverChanged)
    def textColorHover(self) -> QColor:
        """* 获取悬停文字颜色::
            print(obj.textColorHover)

        * 设置选题文字颜色::
            obj.textColorHover = 'red'
            obj.textColorHover = '#ff00ff'
            obj.textColorHover = QColor()
            obj.textColorHover = 100
            obj.textColorHover = (255, 255, 255)
            obj.textColorHover = [255, 255, 255, 255]

        * QSS方式修改::
            obj.setStyleSheet('qproperty-textColorHover: red;')

        * 当值变化时 `textColorHoverChanged` 信号会被发送
        """
        return self.Color.TextColorHover

    @textColorHover.setter
    def textColorHover(self, color: [str, int, tuple, list]):
        self.Color.TextColorHover, color = getColor(
            color), self.Color.TextColorHover
        self.textColorHoverChanged.emit(color, self.Color.TextColorHover)
        self.update()

##########################################################################

    def resetBorderRadius(self):
        """* 重置边框半径"""
        self.borderRadiusChanged.emit(self._borderRadius, 4)  # 发送信号
        self._borderRadius = 4
        self.update()

    @pyqtProperty(float, freset=resetBorderRadius, notify=borderRadiusChanged)
    def borderRadius(self) -> int:
        """* 获取边框半径::
            print(obj.borderRadius)

        * 设置边框半径::
            obj.borderRadius = 4

        * QSS方式修改::
            obj.setStyleSheet('qproperty-borderRadius: 4;')

        * 当值变化时 `borderRadiusChanged` 信号会被发送
        """
        return self._borderRadius

    @borderRadius.setter
    def borderRadius(self, radius: int):
        self._borderRadius, radius = radius, self._borderRadius
        self.borderRadiusChanged.emit(radius, self._borderRadius)
        self.update()

##########################################################################

    def resetBorderWidth(self):
        """* 重置边框宽度"""
        self.borderWidthChanged.emit(self._borderWidth, 0)  # 发送信号
        self._borderWidth = 0
        self.update()

    @pyqtProperty(int, freset=resetBorderWidth, notify=borderWidthChanged)
    def borderWidth(self) -> int:
        """* 获取边框宽度::
            print(obj.borderWidth)

        * 设置边框半径::
            obj.borderWidth = 0

        * QSS方式修改::
            obj.setStyleSheet('qproperty-borderWidth: 0;')

        * 当值变化时 `borderWidthChanged` 信号会被发送
        """
        return self._borderWidth

    @borderWidth.setter
    def borderWidth(self, width: int):
        self._borderWidth, width = width, self._borderWidth
        self.borderWidthChanged.emit(width, self._borderWidth)
        self.update()
