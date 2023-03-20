import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from set import Set
from PyQt5.QtGui import QPixmap, QIcon
import pymysql
from set import Set

class Sauce(QDialog):
    names = []
    curOrderNo = 0
    curbread = 0
    curcheese = 0
    curveg = 0
    cursauce = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_sauce.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.show() # 두번째 창 실행

        self.btnsauce1.clicked.connect(self.btnsauceClicked)
        self.btnsauce2.clicked.connect(self.btnsauceClicked)
        self.btnsauce3.clicked.connect(self.btnsauceClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)
       
    def btnsauceClicked(self):
        print(self.curOrderNo)
        self.conn = pymysql.connect(host='210.119.12.72', user='root', password='12345',
                                    db='sandwich2', charset='utf8')
        print(self.sender().objectName())
        sauceName = self.sender().objectName()

        if sauceName == 'btnsauce1': # 스위트어니언
            sauceVal = 18
        elif sauceName == 'btnsauce2': # 허니머스타드
            sauceVal = 19
        elif sauceName == 'btnsauce3': # 스위트칠리
            sauceVal = 20
        
        query = '''INSERT INTO orderoptions
                        (OrdNo
                       , OptNo)
                    VALUES
                        (%s
                        ,%s)
                '''
        cur = self.conn.cursor()
        cur.execute(query, (self.curOrderNo, sauceVal))
        self.conn.commit()

        self.curOrderOptionNo = cur.lastrowid # OrderOptionNo KEY
        self.conn.close()

        print('메뉴 저장')
        print(self.curbread)
        print(self.curcheese)
        print(self.curveg)
        print(sauceVal)

        self.hide() # 메인 윈도우 숨김
        self.six = Set()
        self.six.names.append(self)
        self.six.curOrderNo = self.curOrderNo
        self.six.curbread = self.curbread
        self.six.curcheese = self.curcheese
        self.six.curveg = self.curveg
        self.six.cursauce = sauceVal
        self.six.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):        
        obj = self.names[0]        
        self.names.pop()
        obj.show()
        self.close()
        
