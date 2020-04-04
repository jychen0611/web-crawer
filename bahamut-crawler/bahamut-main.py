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
#from bahamutcrawler import Cralwer
import requests
# 載入BeautifulSoup套件, 若沒有的話可以先: pip install beautifulsoup4
from bs4 import BeautifulSoup

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
        self.ui.pushButton_4.setText("重新整理")


        self.ui.pushButton.clicked.connect(self.slot_btn_function)
        self.ui.pushButton_2.clicked.connect(self.slot_btn_function_2)
        self.ui.pushButton_3.clicked.connect(self.slot_btn_function_3)
        self.ui.pushButton_4.clicked.connect(self.reset)

    def slot_btn_function(self):
        global state
        state = "title1"
        self.hide()
        self.s = SecondUi()
        self.s.show()
    def slot_btn_function_2(self):
        global state
        state = "title2"
        self.hide()
        self.s = SecondUi()
        self.s.show()
    def slot_btn_function_3(self):
        global state
        state = "title3"
        self.hide()
        self.s = SecondUi()
        self.s.show()




    def reset(self):
        url = 'https://forum.gamer.com.tw/B.php?bsn=60076'
        # 透過request套件抓下這個網址的資料
        requ = requests.get(url)
        # 初步檢視抓到的資料結構
        web_content = requ.text
        # print(web_content)

        # 以 Beautiful Soup 解析 HTML 程式碼 :
        soup = BeautifulSoup(web_content, 'lxml')

        # 找出所有class為"b-list__main__title"的a elements
        titleElements = soup.find_all('a', class_="b-list__main__title")
        # print(titleElements)
        title = [e.text for e in titleElements]
        # print(title)

        # 找出所有class為"b-list__main__title"的p elements
        titleElements = soup.find_all('p', class_="b-list__main__title")
        # print(titleElements)
        title = [e.text for e in titleElements]
        # print(title)

        # 找出所有class為"b-list__brief"的p elements
        briefElements = soup.find_all('p', class_="b-list__brief")
        # print(briefElements)
        brief = [e.text for e in briefElements]
        # print(brief)



        # 找出所有target為"b-list__brief"的a elements
        timeElements = soup.find_all('a', title="觀看最新回覆文章")
        # print(timeElements)
        time = [e.text for e in timeElements]
        # print(time)

        # print數量
        print('文章數量:', len(title), len(brief), len(time))
        global title1, brief1, title2, brief2, title3, brief3
        title1 = title[0]
        brief1 = brief[0]
        title2 = title[1]
        brief2 = brief[1]
        title3 = title[2]
        brief3 = brief[2]



        self.ui.pushButton.setText(title1)
        self.ui.pushButton_2.setText(title2)
        self.ui.pushButton_3.setText(title3)


class SecondUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondUi, self).__init__()
        self.ui = Ui2_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.setText("返回")

        if state == "title1":
            self.ui.label.setText(brief1)
        elif state == "title2":
            self.ui.label.setText(brief2)
        elif state == "title3":
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