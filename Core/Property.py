#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年9月11日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Core.Property
@description: 属性类
"""

from PyQt5.QtCore import pyqtProperty, Qt
from PyQt5.QtGui import QColor

from Core.Colors import MediumGray, Transparent, White
from Core.Template import Template
from Core.Themes import EnumThemes


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Property:

    def __init__(self, *args, **kwargs):
        super(Property, self).__init__(*args, **kwargs)
        self._borderWidth = 0                                 # 默认 普通状态 边框宽度
        self._borderWidthHover = 0                            # 默认 悬停状态 边框宽度
        self._borderWidthPressed = 5                          # 默认 按下状态 边框宽度
        self._borderColor = Transparent                       # 默认 普通状态 边框颜色
        self._borderColorHover = Transparent                  # 默认 悬停状态 边框颜色
        self._borderColorPressed = MediumGray.pressed         # 默认 按下状态 边框颜色
        self._borderRadius = 4                                # 默认 普通状态 圆角半径
        self._borderRadiusHover = 4                           # 默认 悬停状态 圆角半径
        self._borderRadiusPressed = 4                         # 默认 按下状态 圆角半径
        self._textColor = White                               # 默认 普通状态 文字颜色
        self._textColorHover = White.hover                    # 默认 悬停状态 文字颜色
        self._textColorPressed = White.pressed                # 默认 按下状态 文字颜色
        self._backgroundColor = MediumGray                    # 默认 普通状态 文字颜色
        self._backgroundColorHover = MediumGray.hover         # 默认 悬停状态 文字颜色
        self._backgroundColorPressed = MediumGray.pressed     # 默认 按下状态 文字颜色
        self._colorTheme = EnumThemes.MediumGray
        self._resetColorTheme()

    def _resetColorTheme(self):
#         AllThemes[self._colorTheme].update(self)
        self.update()

    def resetBorderWidth(self):
        """重置普通状态下边框宽度"""
        self._borderWidth = 0
        self.update()

    @pyqtProperty(int, freset=resetBorderWidth)
    def borderWidth(self) -> int:
        """获取普通状态下边框宽度"""
        return self._borderWidth

    @borderWidth.setter
    def borderWidth(self, borderWidth: int):
        """设置普通状态下边框宽度"""
        self._borderWidth = borderWidth
        self.update()

    def resetBorderColor(self):
        """重置普通状态下边框颜色"""
        self._borderColor = QColor(Qt.transparent)
        self.update()

    @pyqtProperty(QColor, freset=resetBorderColor)
    def borderColor(self) -> QColor:
        """获取普通状态下边框颜色"""
        return self._borderColor

    @borderColor.setter
    def borderColor(self, borderColor: QColor):
        """设置普通状态下边框颜色"""
        self._borderColor = borderColor
        self.update()

    @property
    def _properties(self):
        return {
            '_borderWidth': self._borderWidth,
            '_borderWidthHover': self._borderWidthHover,
            '_borderWidthPressed': self._borderWidthPressed,
            '_borderColor': self._borderColor,
            '_borderColorHover': self._borderColorHover,
            '_borderColorPressed': self._borderColorPressed,
            '_borderRadius': self._borderRadius,
            '_borderRadiusHover': self._borderRadiusHover,
            '_borderRadiusPressed': self._borderRadiusPressed,
            '_textColor': self._textColor,
            '_textColorHover': self._textColorHover,
            '_textColorPressed': self._textColorPressed,
            '_backgroundColor': self._backgroundColor,
            '_backgroundColorHover': self._backgroundColorHover,
            '_backgroundColorPressed': self._backgroundColorPressed,
        }

    def generateStyle(self):
        if not hasattr(self, 'StyleTpl') or not hasattr(self.StyleTpl, 'generate'):
            return self.styleSheet()
        return self.StyleTpl.generate(**self._properties).decode()


if __name__ == '__main__':
    print(Template('border: {{ borderWidth }}px solid {{ borderColor }};'
                   ).generate(borderWidth=2, borderColor='red').decode())
