import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from veg import Veg

class Cheese(QDialog):
    names = [] 
    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_cheese.ui', self)

        self.btncheese1.clicked.connect(self.btnmenuClicked)
        self.btncheese2.clicked.connect(self.btnmenuClicked)
        self.btncheese3.clicked.connect(self.btnmenuClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)

    def btnmenuClicked(self):
        self.hide() # 메인 윈도우 숨김
        self.four = Veg()
        self.four.names.append(self)
        self.four.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):        
        obj = self.names[0]
        self.names.pop()        
        obj.show()
        self.close()

