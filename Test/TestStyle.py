#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年7月10日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Test.TestStyle
@description: 
"""
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        uic.loadUi('untitled.ui', self)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from QFlatStyle import QFlatStyle  # @UnresolvedImport
    QApplication.setStyle(QFlatStyle())
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
