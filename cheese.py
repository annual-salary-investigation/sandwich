import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


class Cheese(QDialog,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_cheese.ui', self)

        self.show() # tp번째 창 실행