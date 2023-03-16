import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


class Bread(QDialog,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_bread.ui', self)

        self.show() # 두번째 창 실행
