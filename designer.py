#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 2018年3月8日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: designer
# description: 带插件的设计师


from distutils.sysconfig import get_python_lib
import os
import sys

import PyQt5
from PyQt5.QtCore import QProcessEnvironment, QProcess, QLibraryInfo


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


def main():
    if sys.version_info < (3, 5):
        raise RuntimeError('This package requires Python 3.5 or later')

    site_packages = get_python_lib()
    print('site_packages', site_packages)
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    print('current_dir', current_dir)

    env = QProcessEnvironment.systemEnvironment()
    PATH = '{0};{1};{2}'.format(os.path.dirname(
        PyQt5.__file__), sys.prefix, env.value('PATH', ''))
    env.insert('PATH', PATH)
    env.insert('PYQTDESIGNERPATH', os.path.join(current_dir, 'Plugins'))
    env.insert('PYTHONPATH', os.path.join(current_dir))

    print('PATH', env.value('PATH', ''))
    print('PYQTDESIGNERPATH', env.value('PYQTDESIGNERPATH', ''))
    print('PYTHONPATH', env.value('PYTHONPATH', ''))

    ext = '.exe' if os.name == 'nt' else ''
    designer = QProcess()
    designer.setProcessEnvironment(env)

    # for PyQt5.5 latter,pyqt5-tools maybe have problem
    designer_bin = QLibraryInfo.location(
        QLibraryInfo.BinariesPath) + os.sep + 'designer' + ext
    print('designer_bin', designer_bin)

    if os.path.exists(designer_bin):
        designer.start(designer_bin)
        designer.waitForFinished(-1)
        sys.exit(designer.exitCode())
    else:
        raise Exception('Can not find designer')


if __name__ == '__main__':
    main()
