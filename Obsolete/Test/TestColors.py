#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年4月20日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Test.TestColors
@description: 测试颜色
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QHBoxLayout,\
    QVBoxLayout

from Core.Colors import allColors


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class Card(QWidget):

    def __init__(self, name, default, lighter, *args, **kwargs):
        super(Card, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setMinimumSize(130, 100)
        self.setStyleSheet("""
        Card {
            background-color: white;
            border: none;
            border-radius: 4px;
        }
        """)
        hlayout = QHBoxLayout()
        hlayout.addWidget(QLabel(self, styleSheet="""
            background-color: {0};
            border-top-left-radius: 4px;
        """.format(default)))
        hlayout.addWidget(QLabel(self, styleSheet="""
            background-color: {0};
            border-top-right-radius: 4px;
        """.format(lighter)))

        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(hlayout)
        layout.addWidget(QLabel('{0}\n{1},{2}'.format(name, default, lighter)))


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QGridLayout(self)
        colors = allColors()[1:]  # 去掉第一个白色的

        for row, _colors in enumerate((colors[i:i + 6] for i in range(len(colors)) if i % 6 == 0)):
            for col, color in enumerate(_colors):
                layout.addWidget(
                    Card(color.__name__, *color.backgroundColors()), row, col)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setApplicationName('Colors')
    w = Window()
    w.show()
    sys.exit(app.exec_())
