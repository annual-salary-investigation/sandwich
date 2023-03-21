import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from sauce import Sauce
from PyQt5.QtGui import QPixmap, QIcon
import pymysql

class Veg(QDialog):
    names = []
    curOrderNo = 0
    curmenu = 0
    curbread = 0
    curcheese = 0
    curveg = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_Veg.ui', self)
        self.setWindowTitle('샌드위치 먹을래? v0.1')

        self.btnveg1.clicked.connect(self.btnvegClicked)
        self.btnveg2.clicked.connect(self.btnvegClicked)
        self.btnveg3.clicked.connect(self.btnvegClicked)
        self.btnveg4.clicked.connect(self.btnvegClicked)
        self.btnveg5.clicked.connect(self.btnvegClicked)
        self.btnveg6.clicked.connect(self.btnvegClicked)
        self.btnveg7.clicked.connect(self.btnvegClicked)
        self.btnveg8.clicked.connect(self.btnvegClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)

    def btnvegClicked(self):
        print(self.curOrderNo)
        self.conn = pymysql.connect(host='210.119.12.72', user='root', password='12345',
                                    db='sandwich2', charset='utf8')
        print(self.sender().objectName())
        vegName = self.sender().objectName()

        if vegName == 'btnveg1': # 양상추
            vegVal = 10
        elif vegName == 'btnveg2': # 아보카도
            vegVal = 11
        elif vegName == 'btnveg3': # 양파
            vegVal = 12
        elif vegName == 'btnveg4': # 오이
            vegVal = 13
        elif vegName == 'btnveg5': # 올리브
            vegVal = 14
        elif vegName == 'btnveg6': # 토마토
            vegVal = 15
        elif vegName == 'btnveg7': # 피망
            vegVal = 16
        elif vegName == 'btnveg8': # 할라피뇨
            vegVal = 17
        
        query = '''INSERT INTO orderoptions
                        (OrdNo
                       , OptNo)
                    VALUES
                        (%s
                        ,%s)
                '''
        cur = self.conn.cursor()
        cur.execute(query, (self.curOrderNo, vegVal))
        self.conn.commit()

        self.curOrderOptionNo = cur.lastrowid # OrderOptionNo KEY
        self.conn.close()

        print('메뉴 저장')
        print('메뉴',self.curmenu)
        print('빵',self.curbread)
        print('치즈',self.curcheese)

        self.hide() # 메인 윈도우 숨김
        self.sauce = Sauce()
        self.sauce.names.append(self)
        self.sauce.curOrderNo = self.curOrderNo # OrdNo 넘겨줌
        self.sauce.curmenu = self.curmenu
        self.sauce.curbread = self.curbread
        self.sauce.curcheese = self.curcheese
        self.sauce.curveg = vegVal
        self.sauce.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):        
        obj = self.names[0]
        self.names.pop()       
        obj.show()
        self.close()