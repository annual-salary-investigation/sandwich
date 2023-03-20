import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from set import Set

class Sauce(QDialog):
    names = []
    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_sauce.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.show() # 두번째 창 실행

        self.btnsauce1.clicked.connect(self.btnbreadClicked)
        self.btnsauce2.clicked.connect(self.btnbreadClicked)
        self.btnsauce3.clicked.connect(self.btnbreadClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)
       

    def btnbreadClicked(self):
        self.hide() # 메인 윈도우 숨김
        self.six = Set()
        self.six.names.append(self)
        self.six.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):        
        obj = self.names[0]        
        self.names.pop()
        obj.show()
        self.close()
        
