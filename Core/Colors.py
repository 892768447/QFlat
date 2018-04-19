#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


# Created on 2018年4月16日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Core.Colors
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class _Color(QColor):

    def __init__(self, *args, default=None, lighter=None, **kwargs):
        try:
            default, lighter = (default, lighter) if (
                default and lighter) else self.backgroundColors()
            super(_Color, self).__init__(default)
            self.BackgroundColor = self
            self.BackgroundColorHover = QColor(lighter)
            self.BorderColor = self
            self.BorderColorHover = self

            defaultT, lighterT = self.textColors()
            self.TextColor = QColor(defaultT)
            self.TextColorHover = QColor(lighterT)
        except Exception as e:
            print(e)
            super(_Color, self).__init__(*args, **kwargs)

    def __getattribute__(self, name):
        try:
            return super(_Color, self).__getattribute__(name)
        except:
            return QColor()

    def backgroundColors(self):
        return (Qt.white, Qt.white)

    def textColors(self):
        return (Qt.white, Qt.white)


class BlueJeans(_Color):

    def backgroundColors(self):
        return ('#4A89DC', '#5D9CEC')


class Aqua(_Color):

    def backgroundColors(self):
        return ('#3BAFDA', '#4FC1E9')


class Mint(_Color):

    def backgroundColors(self):
        return ('#37BC9B', '#48CFAD')


class Grass(_Color):

    def backgroundColors(self):
        return ('#8CC152', '#A0D468')


class Sunflower(_Color):

    def backgroundColors(self):
        return ('#F6BB42', '#FFCE54')


class Bittersweet(_Color):

    def backgroundColors(self):
        return ('#E9573F', '#FC6E51')


class Grapefruit(_Color):

    def backgroundColors(self):
        return ('#DA4453', '#ED5565')


class Lavender(_Color):

    def backgroundColors(self):
        return ('#967ADC', '#AC92EC')


class PinkRose(_Color):

    def backgroundColors(self):
        return ('#D770AD', '#EC87C0')


class LightGray(_Color):

    def backgroundColors(self):
        return ('#E6E9ED', '#F5F7FA')

    def textColors(self):
        return (Qt.black, Qt.black)


class MediumGray(_Color):

    def backgroundColors(self):
        return ('#AAB2BD', '#CCD1D9')


class DarkGray(_Color):

    def backgroundColors(self):
        return ('#434A54', '#656D78')


class White(_Color):

    def backgroundColors(self):
        return ("#FFFFFF", "#CCD1D9")

    def textColors(self):
        return (Qt.black, Qt.black)


def getColor(color: [str, int, tuple, list]) -> QColor:
    """* 根据给定的参数返回颜色::

            getColor('red')
            getColor('#ff00ff')
            getColor(QColor())
            getColor(100)
            getColor((255, 255, 255))
            getColor([255, 255, 255, 255])

    :param color: str, int, tuple, list
    :return: QColor
    """
    if isinstance(color, _Color):
        return color
    if isinstance(color, QColor):
        return color
    elif isinstance(color, tuple) or isinstance(color, list):
        for c in color:
            if not isinstance(c, int):
                return White()
        if len(color) == 3 or len(color) == 4:
            return QColor(*color)
    elif isinstance(color, int):
        return QColor(color)
    elif isinstance(color, str):
        return QColor(color)
    else:
        return White()


def allColors():
    """第一个为默认颜色"""
    return [
        White, BlueJeans, Aqua, Mint, Grass, Sunflower, Bittersweet,
        Grapefruit, Lavender, PinkRose, LightGray, MediumGray, DarkGray
    ]