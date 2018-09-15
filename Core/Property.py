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

from PyQt5.QtCore import pyqtProperty

from Core.Template import Template


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Property:

    def __init__(self, *args, **kwargs):
        super(Property, self).__init__(*args, **kwargs)
        self._borderWidth = 0                           # 默认 普通状态 边框宽度
        self._borderWidthHover = 0                      # 默认 悬停状态 边框宽度
        self._borderWidthPressed = 0                    # 默认 按下状态 边框宽度
        self._borderColor = 0                           # 默认 普通状态 边框颜色
        self._borderColorHover = 0                      # 默认 悬停状态 边框颜色
        self._borderColorPressed = 0                    # 默认 按下状态 边框颜色
        self._borderRadius = 4                          # 默认 普通状态 圆角半径
        self._borderRadiusHover = 4                     # 默认 悬停状态 圆角半径
        self._borderRadiusPressed = 4                   # 默认 按下状态 圆角半径
        self._textColor = 1                             # 默认 普通状态 文字颜色
        self._textColorHover = 1                        # 默认 悬停状态 文字颜色
        self._textColorPressed = 1                      # 默认 按下状态 文字颜色
        self._backgroundColor = 1                             # 默认 普通状态 文字颜色
        self._backgroundColorHover = 1                        # 默认 悬停状态 文字颜色
        self._backgroundColorPressed = 1                      # 默认 按下状态 文字颜色

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

    @property
    def _properties(self):
        return {
            'borderWidth': self._borderWidth,
            'borderWidthHover': self._borderWidthHover,
            'borderWidthPressed': self._borderWidthPressed,
        }

    def generateStyle(self):
        if not hasattr(self, 'StyleTpl') or not hasattr(self.StyleTpl, 'generate'):
            return self.styleSheet()
        return self.StyleTpl.generate(**self._properties)


if __name__ == '__main__':
    print(Template('border: {{ borderWidth }}px solid {{ borderColor }};'
                   ).generate(borderWidth=2, borderColor='red').decode())
