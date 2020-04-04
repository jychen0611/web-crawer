# -*- coding: utf-8 -*-
'''
巴哈姆特場外休憩區文章列表
多窗口反覆切换，只用PyQt5實現
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from bahamutui import Ui_MainWindow
from bahamutui2 import Ui2_MainWindow

title1 = "title1"
title2 = "title2"
title3 = "title3"
brief1 = "brief1"
brief2 = "brief2"
brief3 = "brief3"
state = "NULL"
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText("巴哈姆特場外休憩區")

        self.ui.pushButton.setText(title1)
        self.ui.pushButton_2.setText(title2)
        self.ui.pushButton_3.setText(title3)


        self.ui.pushButton.clicked.connect(self.slot_btn_function)
        self.ui.pushButton_2.clicked.connect(self.slot_btn_function_2)
        self.ui.pushButton_3.clicked.connect(self.slot_btn_function_3)

    def slot_btn_function(self):
        global state
        state = title1
        self.hide()
        self.s = SecondUi()
        self.s.show()
    def slot_btn_function_2(self):
        global state
        state = title2
        self.hide()
        self.s = SecondUi()
        self.s.show()
    def slot_btn_function_3(self):
        global state
        state = title3
        self.hide()
        self.s = SecondUi()
        self.s.show()


class SecondUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondUi, self).__init__()
        self.ui = Ui2_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.setText("返回")

        if state == title1:
            self.ui.label.setText(brief1)
        elif state == title2:
            self.ui.label.setText(brief2)
        elif state == title3:
            self.ui.label.setText(brief3)



        self.ui.pushButton.clicked.connect(self.slot_btn_function)

    def slot_btn_function(self):
        self.hide()
        self.f = MainWindow()
        self.f.show()


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()