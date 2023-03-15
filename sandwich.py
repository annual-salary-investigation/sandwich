# 샌드위치 키오스크 앱
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QMainWindow):
    conn = None
    curIdx = 0 # 현재 데티어 PK

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/addressBook.ui',self)
        self.setWindowIcon(QIcon('./studyPyQt/addressBook.png'))
        self.setWindowTitle('주소록 v0.5')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())        