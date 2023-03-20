# 샌드위치 키오스크 앱
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from bread import Bread

class qtApp(QDialog):
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

    def btnmenuClicked(self):
        self.hide() # 메인 윈도우 숨김
        self.second = Bread()
        self.second.names.append(self)
        self.second.show() # 두번째 창닫을 때까지 기다림  ## exec --> show      
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())        

    