#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年4月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Core.Colors
@description: 颜色类
"""
from PyQt5.QtGui import QColor


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Color(QColor):

    def __init__(self, *args, hover=None, pressed=None, **kwargs):
        '''
        :param hover: 悬停颜色
        :param pressed: 按下颜色
        '''
        super(Color, self).__init__(*args, **kwargs)
        self.hover = hover or self
        self.pressed = pressed or self

    def toRgba(self):
        """返回rgba格式，如：255, 255, 255, 255"""
        return '{}, {}, {}, {}'.format(self.red(), self.green(), self.blue(), self.alpha())


BlueJeans = Color('#4A89DC', hover=Color('#5D9CEC'))
Aqua = Color('#3BAFDA', hover=Color('#4FC1E9'))
Mint = Color('#37BC9B', hover=Color('#48CFAD'))
Grass = Color('#8CC152', hover=Color('#A0D468'))
Sunflower = Color('#F6BB42', hover=Color('#FFCE54'))
Bittersweet = Color('#E9573F', hover=Color('#FC6E51'))
Grapefruit = Color('#DA4453', hover=Color('#ED5565'))
Lavender = Color('#967ADC', hover=Color('#AC92EC'))
PinkRose = Color('#D770AD', hover=Color('#EC87C0'))
LightGray = Color('#E6E9ED', hover=Color('#F5F7FA'))
MediumGray = Color('#AAB2BD', hover=Color('#CCD1D9'))
DarkGray = Color('#434A54', hover=Color('#656D78'))
White = Color(255, 255, 255, hover=Color('#CCD1D9'), pressed=Color('#CCD1D9'))
Black = Color(0, 0, 0)
Transparent = Color(255, 255, 255, 0)


def getColor(color: [str, int, QColor]) -> QColor:
    """根据给定的参数返回颜色"""
    if isinstance(color, Color):
        return color
    if isinstance(color, QColor):
        return Color(color)
    elif isinstance(color, int):
        return Color(color)
    elif isinstance(color, str):
        return Color(color)
    else:
        return White
