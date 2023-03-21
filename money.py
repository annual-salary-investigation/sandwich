import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


class Money(QDialog):
    names = []

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_money.ui', self)
        self.setWindowIcon(QIcon('./Git_Image/sandwich.png'))
        self.setWindowTitle('샌드위치 먹을래? v0.2')

        self.show() # 두번째 창 실행

        self.btncard.clicked.connect(self.btnbreadClicked)
        self.btnmoney.clicked.connect(self.btnbreadClicked)
        # # #self.btnPrev.clicked.connect(self.btnPrevClicked)

    def btnbreadClicked(self):
        qmsBox = QMessageBox()
        qmsBox.question(self, '결제', '결제를 진행하시겠습니까?',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if qmsBox == QMessageBox.Yes:
            pass
        elif qmsBox == QMessageBox.No:
            pass
        

    