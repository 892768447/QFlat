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


class ThemeWhite:

    def update(self, obj):
        obj._borderWidth = 1                                     # 默认 边框宽度
        obj._borderColor = Colors.MediumGray                     # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.MediumGray                # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.MediumGray              # 默认 按下状态 边框颜色
        obj._textColor = Colors.Black                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.White                      # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.MediumGray.hover      # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.MediumGray.hover    # 默认 按下状态 文字颜色


class ThemeBlueJeans:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.BlueJeans.pressed       # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.BlueJeans                  # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.BlueJeans.hover       # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.BlueJeans.pressed   # 默认 按下状态 文字颜色


class ThemeAqua:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.Aqua.pressed            # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.Aqua                       # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.Aqua.hover            # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.Aqua.pressed        # 默认 按下状态 文字颜色


class ThemeMint:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.Mint.pressed            # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.Mint                       # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.Mint.hover            # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.Mint.pressed        # 默认 按下状态 文字颜色


class ThemeGrass:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.Grass.pressed           # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.Grass                      # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.Grass.hover           # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.Grass.pressed       # 默认 按下状态 文字颜色


class ThemeSunflower:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.Sunflower.pressed       # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.Sunflower                  # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.Sunflower.hover       # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.Sunflower.pressed   # 默认 按下状态 文字颜色


class ThemeBittersweet:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.Bittersweet.pressed     # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.Bittersweet                # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.Bittersweet.hover     # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.Bittersweet.pressed  # 默认 按下状态 文字颜色


class ThemeGrapefruit:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.Grapefruit.pressed      # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.Grapefruit                 # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.Grapefruit.hover      # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.Grapefruit.pressed  # 默认 按下状态 文字颜色


class ThemeLavender:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.Lavender.pressed        # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.Lavender                   # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.Lavender.hover        # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.Lavender.pressed    # 默认 按下状态 文字颜色


class ThemePinkRose:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.PinkRose.pressed        # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.PinkRose                   # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.PinkRose.hover        # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.PinkRose.pressed    # 默认 按下状态 文字颜色


class ThemeLightGray:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.LightGray.pressed       # 默认 按下状态 边框颜色
        obj._textColor = Colors.Black                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.Black                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.Black                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.LightGray                  # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.LightGray.hover       # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.LightGray.pressed   # 默认 按下状态 文字颜色


class ThemeMediumGray:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.MediumGray.pressed      # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White                       # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White                     # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.MediumGray                 # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.MediumGray.hover      # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.MediumGray.pressed  # 默认 按下状态 文字颜色


class ThemeDarkGray:

    def update(self, obj):
        obj._borderColor = Colors.Transparent                    # 默认 普通状态 边框颜色
        obj._borderColorHover = Colors.Transparent               # 默认 悬停状态 边框颜色
        obj._borderColorPressed = Colors.DarkGray.pressed        # 默认 按下状态 边框颜色
        obj._textColor = Colors.White                            # 默认 普通状态 文字颜色
        obj._textColorHover = Colors.White.hover                 # 默认 悬停状态 文字颜色
        obj._textColorPressed = Colors.White.pressed             # 默认 按下状态 文字颜色
        obj._backgroundColor = Colors.DarkGray                   # 默认 普通状态 文字颜色
        obj._backgroundColorHover = Colors.DarkGray.hover        # 默认 悬停状态 文字颜色
        obj._backgroundColorPressed = Colors.DarkGray.pressed    # 默认 按下状态 文字颜色


EnumThemesColors = {
    0:  ThemeWhite(),
    1:  ThemeBlueJeans(),
    2:  ThemeAqua(),
    3:  ThemeMint(),
    4:  ThemeGrass(),
    5:  ThemeSunflower(),
    6: ThemeBittersweet(),
    7:  ThemeGrapefruit(),
    8:  ThemeLavender(),
    9:  ThemePinkRose(),
    10:  ThemeLightGray(),
    11:  ThemeMediumGray(),
    12:  ThemeDarkGray()
}


class EnumThemes:
    White = 0
    BlueJeans = 1
    Aqua = 2
    Mint = 3
    Grass = 4
    Sunflower = 5
    Bittersweet = 6
    Grapefruit = 7
    Lavender = 8
    PinkRose = 9
    LightGray = 10
    MediumGray = 11
    DarkGray = 12


AllThemes = [
    ThemeWhite, ThemeBlueJeans, ThemeAqua, ThemeMint,
    ThemeGrass, ThemeSunflower, ThemeBittersweet, ThemeGrapefruit,
    ThemeLavender, ThemePinkRose, ThemeLightGray, ThemeMediumGray, ThemeDarkGray
]
