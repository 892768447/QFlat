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

    White, BlueJeans, Aqua, Mint, Grass, Sunflower, Bittersweet, \
        Grapefruit, Lavender, PinkRose, LightGray, MediumGray, \
        DarkGray = range(13)

    def __init__(self, *args, **kwargs):
        super(Property, self).__init__(*args, **kwargs)
        self._borderWidth = 0                           # 默认普通状态边框宽度
        self._borderWidthHover = 0                      # 默认悬停状态边框宽度
        self._borderWidthPressed = 0                    # 默认按下状态边框宽度
        self._borderRadius = 4                          # 默认圆角半径

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

    def styleSheet(self):
        return self.StyleTpl.generate(**self._properties)


if __name__ == '__main__':
    print(Template('border: {{ borderWidth }}px solid {{ borderColor }};'
                   ).generate(borderWidth=2, borderColor='red').decode())
