__author__ = 'jefftsai'

import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

form = uic.loadUiType("ui/main.ui")[0]

class mainWindow(QtWidgets.QMainWindow,form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.load_image_pushButton.clicked.connect(self.load_image_pushButton_clicked)
    def load_image_pushButton_clicked(self):
        print("open")


app = QtWidgets.QApplication(sys.argv)
ui = mainWindow()
ui.show()
app.exec_()