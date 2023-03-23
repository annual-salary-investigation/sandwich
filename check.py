import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic
from money import Money

class Check(QDialog):
    names = []
    curOrderNo = 0
    curmenu = 0
    curbread = 0
    curcheese = 0
    curveg = 0
    cursauce = 0
    curset = 0
    total_menu = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_check.ui', self)
        self.setWindowIcon(QIcon('./Git_Image/sandwich.png'))
        self.setWindowTitle('샌드위치 먹을래? v0.2')

        self.show() # 두번째 창 실행
        
        self.btnpay.clicked.connect(self.btncheckClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)
       

    def btncheckClicked(self):
        self.hide() # 메인 윈도우 숨김
        self.money = Money()
        self.money.names.append(self)
        self.money.curOrderNo = self.curOrderNo
        self.money.curmenu = self.curmenu
        self.money.curbread = self.curbread
        self.money.curcheese = self.curcheese
        self.money.curveg = self.curveg
        self.money.cursauce = self.cursauce
        self.money.curset = self.curset
       

        self.money.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐
    
    def btnPrevClicked(self):        
        obj = self.names[0]        
        self.names.pop()
        obj.show()
        self.close()
        
