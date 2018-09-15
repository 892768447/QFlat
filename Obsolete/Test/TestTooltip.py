#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年7月8日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Test.TestTooltip
@description: 
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from Widgets.ToolTip import ToolTip


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        btn = QPushButton('按钮', self, clicked=self.onClick)
        btn.setObjectName('haha')
        btn.setToolTip('aaa')
        layout.addWidget(btn)

    def onClick(self):
        ToolTip.showText(self.sender(), 'text')


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
