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

    color = Colors.Transparent

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeWhite:

    color = Colors.White

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeBlueJeans:

    color = Colors.BlueJeans

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeAqua:

    color = Colors.Aqua

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeMint:

    color = Colors.Mint

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeGrass:

    color = Colors.Grass

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeSunflower:

    color = Colors.Sunflower

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeBittersweet:

    color = Colors.Bittersweet

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeGrapefruit:

    color = Colors.Grapefruit

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeLavender:

    color = Colors.Lavender

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemePinkRose:

    color = Colors.PinkRose

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeLightGray:

    color = Colors.LightGray

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeMediumGray:

    color = Colors.MediumGray

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class ThemeDarkGray:

    color = Colors.DarkGray

    def __init__(self, obj):
        self.obj = obj

    def update(self):
        pass


class Int(int):

    def __new__(self, value, theme):
        obj = int.__new__(self, value)
        obj.theme = theme
        return obj

    def __repr__(self):
        return 'Int({}, {})'.format(int(self), self.color)


class EnumThemes:
    Transparent = Int(0, ThemeTransparent)
    White = Int(1, ThemeWhite)
    BlueJeans = Int(2, ThemeBlueJeans)
    Aqua = Int(3, ThemeAqua)
    Mint = Int(4, ThemeMint)
    Grass = Int(5, ThemeGrass)
    Sunflower = Int(6, ThemeSunflower)
    Bittersweet = Int(7, ThemeBittersweet)
    Grapefruit = Int(8, ThemeGrapefruit)
    Lavender = Int(9, ThemeLavender)
    PinkRose = Int(10, ThemePinkRose)
    LightGray = Int(1, ThemeLightGray)
    MediumGray = Int(12, ThemeMediumGray)
    DarkGray = Int(13, ThemeDarkGray)

AllThemes = [
    ThemeTransparent, ThemeWhite, ThemeBlueJeans, ThemeAqua, ThemeMint,
    ThemeGrass, ThemeSunflower, ThemeBittersweet, ThemeGrapefruit,
    ThemeLavender, ThemePinkRose, ThemeLightGray, ThemeMediumGray, ThemeDarkGray
]
