import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic



class Sauce(QDialog,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_set.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.show() # 두번째 창 실행

        self.btnbread1.clicked.connect(self.btnbreadClicked)
        self.btnbread2.clicked.connect(self.btnbreadClicked)
        self.btnbread3.clicked.connect(self.btnbreadClicked)
        self.btnbread4.clicked.connect(self.btnbreadClicked)
        self.btnbread5.clicked.connect(self.btnbreadClicked)
        self.btnbread6.clicked.connect(self.btnbreadClicked)

    def btnbreadClicked(self):
        self.hide() # 메인 윈도우 숨김
        # self.third = Set()
        # self.third.exec() # 두번째 창닫을 때까지 기다림
        self.show() # 두번째 창 닫으면 다시 첫번 째 창 보여짐
        
