import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from cheese import Cheese
from PyQt5.QtGui import QPixmap, QIcon
import pymysql

class Bread(QDialog):
    names = []
    curOrderNo = 0
    curmenu = 0
    breadVal=0
    total_menu = 0
    

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_bread.ui', self)
        self.setWindowIcon(QIcon('./Git_Image/sandwich.png'))
        self.setWindowTitle('샌드위치 먹을래? v0.2')

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


        if breadName == 'btnbread1': # 화이트
            breadVal = 1
        elif breadName == 'btnbread2': # 하티
            breadVal = 2
        elif breadName == 'btnbread3': # 위트
            breadVal = 3
        elif breadName == 'btnbread4': # 파마산 오래가노
            breadVal = 4
        elif breadName == 'btnbread5': # 허니오트
            breadVal = 5
        elif breadName == 'btnbread6': # 플랫브래드
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
        print('메뉴',self.curmenu)
    
        self.hide() # 메인 윈도우 숨김
        self.cheese = Cheese()
        self.cheese.names.append(self)
        self.cheese.curOrderNo = self.curOrderNo # OrdNo 넘겨줌
        self.cheese.curmenu = self.curmenu
        self.cheese.curbread = breadVal

        if self.curmenu == 4: # 
            self.cheese.total_menu = '메뉴 선택 : 이탈리안 비엠티'
            self.cheese.menuview.setText(self.cheese.total_menu)
        elif self.curmenu ==3:
            self.cheese.total_menu = '메뉴 선택 : 에그마요'
            self.cheese.menuview.setText(self.cheese.total_menu)
        elif self.curmenu ==2:
            self.cheese.total_menu = '메뉴 선택 : 스테이크 & 치즈'
            self.cheese.menuview.setText(self.cheese.total_menu)
        elif self.curmenu ==1:
            self.cheese.total_menu = '메뉴 선택 : 서브웨이 클럽'
            self.cheese.menuview.setText(self.cheese.total_menu)
        elif self.curmenu ==5:
            self.cheese.total_menu = '메뉴 선택 : 치킨 데리야끼'
            self.cheese.menuview.setText(self.cheese.total_menu)

        # 빵
        if breadVal == 1: 
            self.cheese.total_menu = '빵 선택 : 화이트'
            self.cheese.menuview.append(self.cheese.total_menu)
        elif breadVal ==2:
            self.cheese.total_menu = '빵 선택 : 하티'
            self.cheese.menuview.append(self.cheese.total_menu)
        elif breadVal ==3:
            self.cheese.total_menu = '빵 선택 : 위트'
            self.cheese.menuview.append(self.cheese.total_menu)
        elif breadVal ==4:
            self.cheese.total_menu = '빵 선택 : 파마산 오래가노'
            self.cheese.menuview.append(self.cheese.total_menu)
        elif breadVal ==5:
            self.cheese.total_menu = '빵 선택 : 허니오트'
            self.cheese.menuview.append(self.cheese.total_menu)
        elif breadVal ==6:
            self.cheese.total_menu = '빵 선택 : 플랫브래드'
            self.cheese.menuview.append(self.cheese.total_menu)


        self.cheese.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):
        obj = self.names[0]
        self.names.pop()
        obj.show()
        self.close()

        
