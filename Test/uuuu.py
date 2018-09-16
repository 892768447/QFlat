# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Button = Button(Form)
        self.Button.setGeometry(QtCore.QRect(130, 60, 90, 30))
        self.Button.setObjectName("Button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Button.setStyleSheet(_translate("Form", "/*QFlat Button Style*/\n"
"QPushButton {\n"
"    width: 90px;\n"
"    height: 30px;\n"
"    border: 0px solid rgba(255, 255, 255, 0);\n"
"    border-radius: 4px;\n"
"    color: rgba(255, 255, 255, 255);\n"
"    background-color: rgba(150, 122, 220, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 0px solid rgba(255, 255, 255, 0);\n"
"    border-radius: 4px;\n"
"    color: rgba(255, 255, 255, 255);\n"
"    background-color: rgba(172, 146, 236, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 5px solid rgba(150, 122, 220, 255);\n"
"    border-radius: 4px;\n"
"    color: rgba(255, 255, 255, 255);\n"
"    background-color: rgba(150, 122, 220, 255);\n"
"}\n"
"    "))

from Widgets.Button import Button

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

