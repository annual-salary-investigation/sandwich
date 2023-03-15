import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_secondwindow = uic.loadUiType("sandwich_bread.ui")[0] #두 번째창 ui
class Bread(QDialog,QWidget,form_secondwindow):
    def __init__(self):
        super(Bread,self).__init__()
        self.initUI()
        self.show() # 두번째창 실행

    def initUI(self):
        self.setupUi(self)