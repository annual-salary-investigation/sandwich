import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from veg import Veg
from PyQt5.QtGui import QPixmap, QIcon
import pymysql

class Cheese(QDialog):
    names = []
    curOrderNo = 0
    curmenu = 0
    curbread = 0
    curcheese = 0
    

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_cheese.ui', self)
        self.setWindowIcon(QIcon('./Git_Image/sandwich.png'))
        self.setWindowTitle('샌드위치 먹을래? v0.2')

        self.btncheese1.clicked.connect(self.btncheeseClicked)
        self.btncheese2.clicked.connect(self.btncheeseClicked)
        self.btncheese3.clicked.connect(self.btncheeseClicked)
        self.btnPrev.clicked.connect(self.btnPrevClicked)
        

    def btncheeseClicked(self):
        print(self.curOrderNo)
        self.conn = pymysql.connect(host='210.119.12.72', user='root', password='12345',
                                    db='sandwich2', charset='utf8')
        print(self.sender().objectName())
        cheeseName = self.sender().objectName()

        if cheeseName == 'btncheese1': # 아메리칸
            cheeseVal = 7
        elif cheeseName == 'btncheese2': # 슈레드
            cheeseVal = 8
        elif cheeseName == 'btncheese3': # 모짜렐라
            cheeseVal = 9

        query = '''INSERT INTO orderoptions
                        (OrdNo
                       , OptNo)
                    VALUES
                        (%s
                        ,%s)
                '''
        cur = self.conn.cursor()
        cur.execute(query, (self.curOrderNo, cheeseVal))
        self.conn.commit()

        self.curOrderOptionNo = cur.lastrowid # OrderOptionNo KEY
        self.conn.close()

        print('메뉴 저장')
        print('메뉴',self.curmenu)
        print('빵',self.curbread)
      

        self.hide() # 메인 윈도우 숨김
        self.veg = Veg()
        self.veg.names.append(self)
        self.veg.curOrderNo = self.curOrderNo # OrdNo 넘겨줌
        self.veg.curmenu = self.curmenu
        self.veg.curbread = self.curbread
        self.veg.curcheese = cheeseVal
        self.veg.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐


    def btnPrevClicked(self):        
        obj = self.names[0]
        self.names.pop()        
        obj.show()
        self.close()
 

