import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
import pymysql
from money import Money

class Set(QDialog,QWidget):
    names = []
    curOrderNo = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_set.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.show() # 두번째 창 실행

        self.btnsingle.clicked.connect(self.btnsetClicked)
        self.btnset.clicked.connect(self.btnsetClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)
       
    def btnsetClicked(self):
        self.conn = pymysql.connect(host='210.119.12.72', user='root', password='12345',
                                    db='sandwich2', charset='utf8')
        print(self.sender().objectName())
        setName = self.sender().objectName()

        if setName == 'btnset': # 세트
            self.setVal = 1
        elif setName == 'btnsingle': # 단품
            self.setVal = 0

        query = '''UPDATE orders
                      SET SetYn = %s
                    WHERE OrdNo = %s       
                '''
        cur = self.conn.cursor()
        cur.execute(query,(self.setVal, self.curOrderNo))
        self.conn.commit()
        self.conn.close()

        print('메뉴 저장')

        
        self.hide() # 메인 윈도우 숨김
        self.seven = Set()
        self.seven.names.append(self)
        self.seven.curOrderNo = self.curOrderNo
        self.seven.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐
    
    def btnPrevClicked(self):
        obj = self.names[0]        
        self.names.pop()
        obj.show()
        self.close()
        
