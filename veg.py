import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from sauce import Sauce


class Veg(QDialog):
    names = [] 

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_Veg.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.btnveg1.clicked.connect(self.btnvegClicked)
        self.btnveg2.clicked.connect(self.btnvegClicked)
        self.btnveg3.clicked.connect(self.btnvegClicked)
        self.btnveg4.clicked.connect(self.btnvegClicked)
        self.btnveg5.clicked.connect(self.btnvegClicked)
        self.btnveg6.clicked.connect(self.btnvegClicked)
        self.btnveg7.clicked.connect(self.btnvegClicked)
        self.btnveg8.clicked.connect(self.btnvegClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)

    def btnvegClicked(self):
        self.hide() # 메인 윈도우 숨김
        self.five = Sauce()
        self.five.names.append(self)
        self.five.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):        
        obj = self.names[0]
        self.names.pop()       
        obj.show()
        self.close()
        
