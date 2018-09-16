"""
Created on 2018年9月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Core.Themes
@description: 
"""
from Core import Colors


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class ThemeTransparent:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeWhite:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeBlueJeans:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeAqua:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeMint:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeGrass:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeSunflower:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeBittersweet:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeGrapefruit:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeLavender:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemePinkRose:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeLightGray:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeMediumGray:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeDarkGray:

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class Int(int):

    def __new__(self, value, color):
        obj = int.__new__(self, value)
        obj.color = color
        return obj

    def __repr__(self):
        return 'Int({}, {})'.format(int(self), self.color)


class EnumThemes:
    Transparent = Int(0,Colors.Transparent)
    White = 1
    BlueJeans = 2
    Aqua = 3
    Mint = 4
    Grass = 5
    Sunflower = 6
    Bittersweet = 7
    Grapefruit = 8
    Lavender = 9
    PinkRose = 10
    LightGray = 11
    MediumGray = 12
    DarkGray = 13

    @classmethod
    def default(cls):
        return cls.MediumGray

AllThemes = [
    ThemeTransparent, ThemeWhite, ThemeBlueJeans, ThemeAqua, ThemeMint,
    ThemeGrass, ThemeSunflower, ThemeBittersweet, ThemeGrapefruit,
    ThemeLavender, ThemePinkRose, ThemeLightGray, ThemeMediumGray, ThemeDarkGray
]
