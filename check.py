import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from money import Money

class Check(QDialog):
    names = []
    curOrderNo = 0
    curbread = 0
    curcheese = 0
    curveg = 0
    cursauce = 0
    curset = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_check.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.show() # 두번째 창 실행

        # print(self.menuview.text())
        # msg="주문내역 : "
        # msg+=str(self.curbread) + self.menuview.text()
        msg='가나다라'
        self.menuview.setText(msg)
        msg+='마바사'
        self.menuview.setText(msg)


        self.btnpay.clicked.connect(self.btnbreadClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)
       

    def btnbreadClicked(self):
        self.hide() # 메인 윈도우 숨김
        self.seven = Money()
        self.seven.names.append(self)
        self.seven.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐
    
    def btnPrevClicked(self):        
        obj = self.names[0]        
        self.names.pop()
        obj.show()
        self.close()
        
