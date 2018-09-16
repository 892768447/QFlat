#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年9月15日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Plugins.Buttonplugin
@description: 按钮设计师插件
"""

from PyQt5.QtCore import Q_ENUMS, pyqtProperty
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin,\
    QPyDesignerPropertySheetExtension, QDesignerFormWindowInterface
from PyQt5.QtGui import QPixmap, QIcon
import sip

from Core.Themes import EnumThemes
from Widgets.Button import Button as _Button
from PyQt5.QtWidgets import QMessageBox


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Button(_Button):
    """设计师里需要枚举,必须在QObject的对象里定义,所以这里重新继承下"""

    Q_ENUMS(EnumThemes)

    def resetColorTheme(self):
        """重置主题"""
        self._colorTheme = self.EnumThemes.MediumGray
        self._resetColorTheme()

    @pyqtProperty(EnumThemes, freset=resetColorTheme)
    def colorTheme(self):
        return self._colorTheme

    @colorTheme.setter
    def colorTheme(self, colorTheme):
        self._colorTheme = colorTheme
        self._resetColorTheme()


Q_TYPEID = {
    'QDesignerPropertySheetExtension': 'org.qt-project.Qt.Designer.PropertySheet'
}


class ButtonPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, *args, **kwargs):
        super(ButtonPlugin, self).__init__(*args, **kwargs)
        self.initialized = False
        QPyDesignerPropertySheetExtension

    def initialize(self, core):
        if self.initialized:
            return
        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def toolTip(self):
        return 'QFlat Button'

    def whatsThis(self):
        return 'QFlat Button'

    def isContainer(self):
        return False

    def createWidget(self, parent):
        button = Button('Button', parent=parent)
        button.styleSheetChanged.connect(self.styleSheetChanged)
        return button

    def name(self):
        return 'Button'

    def group(self):
        return 'QFlat'

    def icon(self):
        return QIcon(_logo_pixmap)

    def includeFile(self):
        return 'QFlat.Widgets.Button'

    def domXml(self):
        return '<widget class="{0}" name="{0}">\n' \
               '</widget>\n'.format(self.name())

    def styleSheetChanged(self):
        widget = self.sender()
        form = QDesignerFormWindowInterface.findFormWindow(widget)
        if form:
            sheet = form.core().extensionManager().extension(
                widget, Q_TYPEID['QDesignerPropertySheetExtension'])
            sheet = sip.cast(sheet, QPyDesignerPropertySheetExtension)
            index = sheet.indexOf('styleSheet')
            sheet.setChanged(index, True)

    def borderRadiusChanged(self):
        pass

    def colorThemeChanged(self):
        pass


# Define the image used for the icon.
_logo_16x16_xpm = [
    '16 16 76 1',
    'k c #9FC6C2',
    '$ c #18A093',
    'i c #D8F5F3',
    '7 c #8AC9C0',
    'G c #A5DDDE',
    'S c #47C1BA',
    'V c #16A093',
    'g c #4EBCB4',
    '3 c #86D5CB',
    'r c #9CE2DE',
    'u c #14A398',
    'L c #19A194',
    'v c #58B8AF',
    'I c #1EA295',
    'E c #1EA296',
    'b c #54C4BA',
    'B c #C5DADA',
    '9 c #4DC3B7',
    '5 c #1CA59B',
    'A c #D9E7DD',
    'o c #1CA296',
    'e c #6CBFB8',
    '6 c #68D1CC',
    'c c #9DD4C4',
    'X c #159E91',
    'C c #DAF7F7',
    'p c #6FC3B7',
    'q c #63C1B6',
    'O c #1FA397',
    's c #55C5BB',
    '; c #74C4B9',
    'N c #44BFBB',
    'z c #1DA69B',
    '+ c #189F92',
    'y c #1DA396',
    'H c #99D1C4',
    '2 c #8DCFC1',
    '& c #1BA094',
    ', c #9CD8CC',
    '< c #DBEFE9',
    'P c #25A599',
    '@ c #19A094',
    '* c #1EA496',
    'T c #23A599',
    'w c #67C0B8',
    'M c #6CBEB7',
    '= c #15A399',
    'm c #65C0B7',
    '  c #26A69A',
    'J c #46BEB6',
    't c #6EB5B7',
    '% c #1AA195',
    '8 c #57BBAA',
    '1 c #9DD3D4',
    'n c #6DC5BB',
    'U c #1DA296',
    'Y c #22A397',
    'F c #70C6B9',
    'R c #20A397',
    '# c #149E92',
    'l c #19A295',
    '0 c #2C9C8F',
    'j c #6AD5D3',
    'Z c #67C2BB',
    'x c #5BC3C5',
    'd c #36A195',
    '> c #B0E4E8',
    '4 c #69B6B9',
    'f c #6FC7BB',
    '. c #26A599',
    'D c #39A295',
    ': c #52B9A8',
    '- c #DAF5F3',
    'h c #65B9B2',
    'K c #A9D4D2',
    'a c #57BAAA',
    '                ',
    '                ',
    '                ',
    '                ',
    '                ',
    '  .XoO+@#$%&*   ',
    ' .=-;:>,<1234*  ',
    ' .567890qwerty  ',
    ' .uipasdfghjkl  ',
    ' .zxcvbdnmMNBV  ',
    ' .=CZASDFGHJKL  ',
    ' .PIUUYTRUEYUP  ',
    '  .PPPPPPPPPP   ',
    '                ',
    '                ',
    '                '
]

_logo_pixmap = QPixmap(_logo_16x16_xpm)
