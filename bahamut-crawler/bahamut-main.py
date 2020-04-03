from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QFrame,QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from bahamutui import Ui_MainWindow
import json
import sys
import random

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())