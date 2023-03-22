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
    curmenu = 0
    curbread = 0
    curcheese = 0
    curveg = 0
    cursauce = 0
    total_menu = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_sauce.ui', self)
        self.setWindowIcon(QIcon('./Git_Image/sandwich.png'))
        self.setWindowTitle('샌드위치 먹을래? v0.2')

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

        if sauceName == 'btnsauce1': # 스위트칠리
            sauceVal = 18
        elif sauceName == 'btnsauce2': # 사우스웨스트
            sauceVal = 19
        elif sauceName == 'btnsauce3': # 렌치드레싱
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
        print('메뉴',self.curmenu)
        print('빵',self.curbread)
        print('치즈',self.curcheese)
        print('야채',self.curveg)


        self.hide() # 메인 윈도우 숨김
        self.set = Set()
        self.set.names.append(self)
        self.set.curOrderNo = self.curOrderNo
        self.set.curmenu = self.curmenu
        self.set.curbread = self.curbread
        self.set.curcheese = self.curcheese
        self.set.curveg = self.curveg
        self.set.cursauce = sauceVal

        if self.curmenu == 4: # 
            self.set.total_menu = '메뉴 선택 : 이탈리안 비엠티'
            self.set.menuview.setText(self.set.total_menu)
        elif self.curmenu ==3:
            self.set.total_menu = '메뉴 선택 : 에그마요'
            self.set.menuview.setText(self.set.total_menu)
        elif self.curmenu ==2:
            self.set.total_menu = '메뉴 선택 : 스테이크 & 치즈'
            self.set.menuview.setText(self.set.total_menu)
        elif self.curmenu ==1:
            self.set.total_menu = '메뉴 선택 : 서브웨이 클럽'
            self.set.menuview.setText(self.set.total_menu)
        elif self.curmenu ==5:
            self.set.total_menu = '메뉴 선택 : 치킨 데리야끼'
            self.set.menuview.setText(self.set.total_menu)

        # 빵
        if self.curbread == 1: 
            self.set.total_menu = '빵 선택 : 화이트'
            self.set.menuview.append(self.set.total_menu)
        elif self.curbread ==2:
            self.set.total_menu = '빵 선택 : 하티'
            self.set.menuview.append(self.set.total_menu)
        elif self.curbread ==3:
            self.set.total_menu = '빵 선택 : 위트'
            self.set.menuview.append(self.set.total_menu)
        elif self.curbread ==4:
            self.set.total_menu = '빵 선택 : 파마산 오래가노'
            self.set.menuview.append(self.set.total_menu)
        elif self.curbread ==5:
            self.set.total_menu = '빵 선택 : 허니오트'
            self.set.menuview.append(self.set.total_menu)
        elif self.curbread ==6:
            self.set.total_menu = '빵 선택 : 플랫브래드'
            self.set.menuview.append(self.set.total_menu)

        # 치즈
        if self.curcheese == 7:  
            self.set.total_menu = '치즈 선택 : 아메리칸 치즈'
            self.set.menuview.append(self.set.total_menu)
        elif self.curcheese ==8:
            self.set.total_menu = '치즈 선택 : 슈레드 치즈'
            self.set.menuview.append(self.set.total_menu)
        elif self.curcheese ==9:
            self.set.total_menu = '치즈 선택 : 모짜렐라 치즈'
            self.set.menuview.append(self.set.total_menu)

        # 야채
        if self.curveg == 10: # 
            self.set.total_menu = '야채 선택 : 양상추'
            self.set.menuview.append(self.set.total_menu)
        elif self.curveg ==11:
            self.set.total_menu = '야채 선택 : 아보카도'
            self.set.menuview.append(self.set.total_menu)
        elif self.curveg ==12:
            self.set.total_menu = '야채 선택 : 양파'
            self.set.menuview.append(self.set.total_menu)
        elif self.curveg ==13:
            self.set.total_menu = '야채 선택 : 오이'
            self.set.menuview.append(self.set.total_menu)
        elif self.curveg ==14:
            self.set.total_menu = '야채 선택 : 올리브'
            self.set.menuview.append(self.set.total_menu)
        elif self.curveg ==15:
            self.set.total_menu = '야채 선택 : 토마토'
            self.set.menuview.append(self.set.total_menu)
        elif self.curveg ==16:
            self.set.total_menu = '야채 선택 : 피망'
            self.set.menuview.append(self.set.total_menu)
        elif self.curveg ==17:
            self.set.total_menu = '야채 선택 : 할라피뇨'
            self.set.menuview.append(self.set.total_menu)

        # 소스
        if sauceVal == 18: # 
            self.set.total_menu = '소스 선택 : 스위트칠리'
            self.set.menuview.append(self.set.total_menu)
        elif sauceVal ==19:
            self.set.total_menu = '소스 선택 : 사우스웨스트'
            self.set.menuview.append(self.set.total_menu)
        elif sauceVal ==20:
            self.set.total_menu = '소스 선택 : 렌치드레싱'
            self.set.menuview.append(self.set.total_menu)

        self.set.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐

    def btnPrevClicked(self):        
        obj = self.names[0]        
        self.names.pop()
        obj.show()
        self.close()
        
