"""
Created on 2018年9月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Core.Themes
@description: 
"""
from Core.Colors import Transparent, MediumGray, White


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Theme(dict):

    Attributes = {
        'borderWidth': 0,                                 # 默认 普通状态 边框宽度
        'borderWidthHover': 0,                            # 默认 悬停状态 边框宽度
        'borderWidthPressed': 5,                          # 默认 按下状态 边框宽度
        'borderColor': Transparent,                       # 默认 普通状态 边框颜色
        'borderColorHover': Transparent,                  # 默认 悬停状态 边框颜色
        'borderColorPressed': MediumGray.pressed,         # 默认 按下状态 边框颜色
        'borderRadius': 4,                               # 默认 普通状态 圆角半径
        'borderRadiusHover': 4,                           # 默认 悬停状态 圆角半径
        'borderRadiusPressed': 4,                         # 默认 按下状态 圆角半径
        'textColor': White,                               # 默认 普通状态 文字颜色
        'textColorHover': White.hover,                    # 默认 悬停状态 文字颜色
        'textColorPressed': White.pressed,                # 默认 按下状态 文字颜色
        'backgroundColor': MediumGray,                    # 默认 普通状态 文字颜色
        'backgroundColorHover': MediumGray.hover,         # 默认 悬停状态 文字颜色
        'backgroundColorPressed': MediumGray.pressed,     # 默认 按下状态 文字颜色
    }

    def __init__(self, attributes=None):
        if attributes and isinstance(attributes, dict):
            for name, value in self.attributes.values():
                self.Attributes[name] = value

    def __getattribute__(self, name):
#         ret = self.Attributes.get(name, None)
#         if ret:
#             return ret
        return super(Theme, self).__getattribute__(name)

    def __str__(self):
        return str(self.Attributes)

ThemeMediumGray = Theme()

if __name__ == '__main__':
    print(ThemeMediumGray.borderColor)
    print(ThemeMediumGray.borderColor1)
