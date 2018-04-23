#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QButtonGroup


# Created on 2018年4月23日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Widgets.ButtonGroup
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class ButtonGroup(QWidget):

    def __init__(self, *args, buttons=None, orientation=Qt.Horizontal, **kwargs):
        super(ButtonGroup, self).__init__(*args, **kwargs)
        # 布局
        layout = QHBoxLayout(
            self, spacing=0) if orientation == Qt.Horizontal else QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.buttonGroup = QButtonGroup(self)
        self.addButtons(buttons)

    def addButton(self, button):
        """添加单个按钮"""
        button.setCheckable(True)
        self.buttonGroup.addButton(button)
        self.layout().addWidget(button)

    def addButtons(self, buttons):
        """添加多个按钮"""
        if not buttons or not isinstance(buttons, (list, tuple)):
            return
        for button in buttons:
            self.addButton(button)
