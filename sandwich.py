# 샌드위치 키오스크 앱
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
import pymysql
from bread import Bread

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich.ui',self)
        self.setWindowIcon(QIcon('./studyPyQt/addressBook.png'))
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.btnmenu1.clicked.connect(self.btnmenuClicked)
        self.btnmenu2.clicked.connect(self.btnmenuClicked)
        self.btnmenu3.clicked.connect(self.btnmenuClicked)
        self.btnmenu4.clicked.connect(self.btnmenuClicked)
        self.btnmenu5.clicked.connect(self.btnmenuClicked)
        self.btnmenu6.clicked.connect(self.btnmenuClicked)

    def btnmenuClicked(self):
        self.hide()
        self.bread = Bread()
        self.bread.exec()
        self.show()
        
        
    
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())        