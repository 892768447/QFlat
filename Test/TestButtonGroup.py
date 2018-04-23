#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QScrollArea

from Core import Colors
from Widgets.Button import Button
from Widgets.ButtonGroup import ButtonGroup


# Created on 2018年4月16日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Test.TestButtonGroup
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('Window{background:rgb(241,242,246);}')
        layout = QVBoxLayout(self)

        colors = Colors.allColors()
        for color in colors:
            widget = ButtonGroup(self)
            for i in range(3):
                c = color()
                btn = Button(c.name() + str(i), widget)
                btn.Color = c
                widget.addButton(btn)
            layout.addWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QScrollArea()
    window.setWidgetResizable(True)
    window.setWidget(Window())
    window.show()
    sys.exit(app.exec_())
