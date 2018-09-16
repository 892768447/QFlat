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

from PyQt5.QtCore import pyqtProperty, pyqtSignal

from Core.Colors import MediumGray, Transparent, White
from Core.Themes import EnumThemes, EnumThemesColors, ThemeMediumGray


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Property(EnumThemes):

    styleSheetChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Property, self).__init__(*args, **kwargs)
        self._borderWidth = 0                                 # 默认 普通状态 边框宽度
        self._borderColor = Transparent                       # 默认 普通状态 边框颜色
        self._borderColorHover = Transparent                  # 默认 悬停状态 边框颜色
        self._borderColorPressed = MediumGray.pressed         # 默认 按下状态 边框颜色
        self._borderRadius = 4                                # 默认 普通状态 圆角半径
        self._textColor = White                               # 默认 普通状态 文字颜色
        self._textColorHover = White.hover                    # 默认 悬停状态 文字颜色
        self._textColorPressed = White.pressed                # 默认 按下状态 文字颜色
        self._backgroundColor = MediumGray                    # 默认 普通状态 文字颜色
        self._backgroundColorHover = MediumGray.hover         # 默认 悬停状态 文字颜色
        self._backgroundColorPressed = MediumGray.pressed     # 默认 按下状态 文字颜色
        self._colorTheme = EnumThemes.MediumGray              # 默认 主题
        self._resetColorTheme()

    def _resetColorTheme(self):
        EnumThemesColors.get(self._colorTheme, ThemeMediumGray()).update(self)
        self.update()

    def resetColorTheme(self):
        """重置主题"""
        self._colorTheme = EnumThemes.MediumGray
        self._resetColorTheme()

    @pyqtProperty(int, freset=resetColorTheme)
    def colorTheme(self):
        return self._colorTheme

    @colorTheme.setter
    def colorTheme(self, colorTheme):
        self._colorTheme = colorTheme
        self._resetColorTheme()

    def resetBorderRadius(self):
        """重置普通状态下边框宽度"""
        self._borderRadius = 4
        self.update()

    @pyqtProperty(int, freset=resetBorderRadius)
    def borderRadius(self) -> int:
        """获取普通状态下边框圆角"""
        return self._borderRadius

    @borderRadius.setter
    def borderRadius(self, borderRadius: int):
        """设置普通状态下边框圆角"""
        self._borderRadius = borderRadius
        self.update()

    def _properties(self):
        return {
            '_borderWidth': self._borderWidth,
            '_borderColor': self._borderColor.toRgba(),
            '_borderColorHover': self._borderColorHover.toRgba(),
            '_borderColorPressed': self._borderColorPressed.toRgba(),
            '_borderRadius': self._borderRadius,
            '_textColor': self._textColor.toRgba(),
            '_textColorHover': self._textColorHover.toRgba(),
            '_textColorPressed': self._textColorPressed.toRgba(),
            '_backgroundColor': self._backgroundColor.toRgba(),
            '_backgroundColorHover': self._backgroundColorHover.toRgba(),
            '_backgroundColorPressed': self._backgroundColorPressed.toRgba(),
        }

    def generateStyle(self):
        if not hasattr(self, 'StyleTpl') or not hasattr(self.StyleTpl, 'generate'):
            return self.styleSheet()
        self.styleSheetChanged.emit()
        return self.StyleTpl.generate(**self._properties()).decode()
