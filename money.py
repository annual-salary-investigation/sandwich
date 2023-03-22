import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from done import Done


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


    def btnbreadClicked(self):
        result = QMessageBox()
        result.setStyleSheet('QMessageBox {color :rgb(255, 255, 255)}')
        result.setWindowIcon(QIcon('./Git_Image/sandwich.png'))
        qmsBox = result.question(result, '결제', '결제 하시겠습니까?',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
       
        
        if qmsBox == QMessageBox.Yes:
            self.done = Done()
            self.done.names.append(self)
            self.done.show()
            self.close
        elif qmsBox == QMessageBox.No:
            return
        

           
            
        

    