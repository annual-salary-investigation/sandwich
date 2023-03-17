import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from sauce import Sauce


class Veg(QDialog):
    def __init__(self):
        names = [] 
        super().__init__()
        uic.loadUi('./sandwich_Veg.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.show() # 두번째 창 실행

        self.btnveg1.clicked.connect(self.btnbreadClicked)
        self.btnveg2.clicked.connect(self.btnbreadClicked)
        self.btnveg3.clicked.connect(self.btnbreadClicked)
        self.btnveg4.clicked.connect(self.btnbreadClicked)
        self.btnveg5.clicked.connect(self.btnbreadClicked)
        self.btnveg6.clicked.connect(self.btnbreadClicked)
        self.btnveg7.clicked.connect(self.btnbreadClicked)
        self.btnveg8.clicked.connect(self.btnbreadClicked)

    def btnbreadClicked(self):
        self.hide() # 메인 윈도우 숨김
        self.five = Sauce()
        self.five.exec() # 두번째 창닫을 때까지 기다림
        self.show() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):        
        obj = self.names[0]        
        self.hide()
        obj.exec()
        self.close()
        
