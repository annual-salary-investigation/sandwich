import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from cheese import Cheese
from PyQt5.QtGui import QPixmap, QIcon
import pymysql

class Bread(QDialog):
    names = []
    curOrderNo = 0
    breadVal=0

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_bread.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.btnbread1.clicked.connect(self.btnbreadClicked)
        self.btnbread2.clicked.connect(self.btnbreadClicked)
        self.btnbread3.clicked.connect(self.btnbreadClicked)
        self.btnbread4.clicked.connect(self.btnbreadClicked)
        self.btnbread5.clicked.connect(self.btnbreadClicked)
        self.btnbread6.clicked.connect(self.btnbreadClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)

        #self.menuview.setEnabled(False)
        #self.text_value = ''

    def btnbreadClicked(self):
        self.conn = pymysql.connect(host='210.119.12.72', user='root', password='12345',
                                    db='sandwich2', charset='utf8')
        print(self.sender().objectName())
        breadName = self.sender().objectName()


        if breadName == 'btnbread1': # 허니오트
            breadVal = 1
        elif breadName == 'btnbread2': # 화이트
            breadVal = 2
        elif breadName == 'btnbread3': # 플랫브레드
            breadVal = 3
        elif breadName == 'btnbread4': # 위트
            breadVal = 4
        elif breadName == 'btnbread5': # 하티
            breadVal = 5
        elif breadName == 'btnbread6': # 파마산오레가노
            breadVal = 6

        query = '''INSERT INTO orderoptions
                        (OrdNo
                       , OptNo)
                    VALUES
                        (%s
                        ,%s)
                '''
        cur = self.conn.cursor()
        cur.execute(query, (self.curOrderNo, breadVal))
        self.conn.commit()

        self.curOrderOptionNo = cur.lastrowid # OrderOptionNo KEY
        self.conn.close()

        print('메뉴 저장')
    
        self.hide() # 메인 윈도우 숨김
        self.third = Cheese()
        self.third.names.append(self)
        self.third.curOrderNo = self.curOrderNo # OrdNo 넘겨줌
        self.third.curbread = breadVal
        self.third.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):
        obj = self.names[0]
        self.names.pop()
        obj.show()
        self.close()

        
