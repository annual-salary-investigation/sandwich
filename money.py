import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class Money(QDialog):
    names = []
    curOrderNo = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_money.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.show() # 두번째 창 실행

        # self.btncard.clicked.connect(self.btnbreadClicked)
        # self.btnmoney.clicked.connect(self.btnbreadClicked)
        # #self.btnPrev.clicked.connect(self.btnPrevClicked)

    