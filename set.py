import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
import pymysql
from check import Check

class Set(QDialog):
    names = []
    curOrderNo = 0
    curmenu = 0
    curbread = 0
    curcheese = 0
    curveg = 0
    cursauce = 0
    curset = 0
    
    def __init__(self):
        super().__init__()
        uic.loadUi('./sandwich_set.ui', self)
        self.setWindowIcon(QIcon('./Git_Image/sandwich.png'))
        self.setWindowTitle('샌드위치 먹을래? v0.2')

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
            setVal = 1
        elif setName == 'btnsingle': # 단품
            setVal = 0

        query = '''UPDATE orders
                      SET SetYn = %s
                    WHERE OrdNo = %s       
                '''
        cur = self.conn.cursor()
        cur.execute(query,(setVal, self.curOrderNo))
        self.conn.commit()
        self.conn.close()

        print('메뉴 저장')
        print('메뉴',self.curmenu)
        print('빵',self.curbread)
        print('치즈',self.curcheese)
        print('야채',self.curveg)
        print('소스',self.cursauce)

        self.hide() # 메인 윈도우 숨김
        self.check = Check()
        self.check.names.append(self)
        self.check.curOrderNo = self.curOrderNo
        self.check.curmenu = self.curmenu
        self.check.curbread = self.curbread
        self.check.curcheese = self.curcheese
        self.check.curveg = self.curveg
        self.check.cursauce = self.cursauce
        self.check.curset = setName

        print(self.curbread)
        # 메뉴
        if self.curmenu == 4: # 
            self.check.total_menu = '메뉴 선택 : 이탈리안 비엠티'
            self.check.menuview.setText(self.check.total_menu)
        elif self.curmenu ==3:
            self.check.total_menu = '메뉴 선택 : 에그마요'
            self.check.menuview.setText(self.check.total_menu)
        elif self.curmenu ==2:
            self.check.total_menu = '메뉴 선택 : 스테이크 & 치즈'
            self.check.menuview.setText(self.check.total_menu)
        elif self.curmenu ==1:
            self.check.total_menu = '메뉴 선택 : 서브웨이 클럽'
            self.check.menuview.setText(self.check.total_menu)
        elif self.curmenu ==5:
            self.check.total_menu = '메뉴 선택 : 치킨 데리야끼'
            self.check.menuview.setText(self.check.total_menu)

        # 빵
        if self.curbread == 1: # 
            self.check.total_menu = '빵 선택 : 화이트'
            self.check.menuview.append(self.check.total_menu)
        elif self.curbread ==2:
            self.check.total_menu = '빵 선택 : 하티'
            self.check.menuview.append(self.check.total_menu)
        elif self.curbread ==3:
            self.check.total_menu = '빵 선택 : 위트'
            self.check.menuview.append(self.check.total_menu)
        elif self.curbread ==4:
            self.check.total_menu = '빵 선택 : 파마산 오래가노'
            self.check.menuview.append(self.check.total_menu)
        elif self.curbread ==5:
            self.check.total_menu = '빵 선택 : 허니오트'
            self.check.menuview.append(self.check.total_menu)
        elif self.curbread ==6:
            self.check.total_menu = '빵 선택 : 플랫브래드'
            self.check.menuview.append(self.check.total_menu)

        # 치즈
        if self.curcheese == 7: # 
            self.check.total_menu = '치즈 선택 : 아메리칸 치즈'
            self.check.menuview.append(self.check.total_menu)
        elif self.curcheese ==8:
            self.check.total_menu = '치즈 선택 : 슈레드 치즈'
            self.check.menuview.append(self.check.total_menu)
        elif self.curcheese ==9:
            self.check.total_menu = '치즈 선택 : 모짜렐라 치즈'
            self.check.menuview.append(self.check.total_menu)

        # 야채
        if self.curveg == 10: # 
            self.check.total_menu = '야채 선택 : 양상추'
            self.check.menuview.append(self.check.total_menu)
        elif self.curveg ==11:
            self.check.total_menu = '야채 선택 : 아보카도'
            self.check.menuview.append(self.check.total_menu)
        elif self.curveg ==12:
            self.check.total_menu = '야채 선택 : 양파'
            self.check.menuview.append(self.check.total_menu)
        elif self.curveg ==13:
            self.check.total_menu = '야채 선택 : 오이'
            self.check.menuview.append(self.check.total_menu)
        elif self.curveg ==14:
            self.check.total_menu = '야채 선택 : 올리브'
            self.check.menuview.append(self.check.total_menu)
        elif self.curveg ==15:
            self.check.total_menu = '야채 선택 : 토마토'
            self.check.menuview.append(self.check.total_menu)
        elif self.curveg ==16:
            self.check.total_menu = '야채 선택 : 피망'
            self.check.menuview.append(self.check.total_menu)
        elif self.curveg ==17:
            self.check.total_menu = '야채 선택 : 할라피뇨'
            self.check.menuview.append(self.check.total_menu)

        # 소스
        if self.cursauce == 18: # 
            self.check.total_menu = '소스 선택 : 스위트칠리'
            self.check.menuview.append(self.check.total_menu)
        elif self.cursauce ==19:
            self.check.total_menu = '소스 선택 : 사우스웨스트'
            self.check.menuview.append(self.check.total_menu)
        elif self.cursauce ==20:
            self.check.total_menu = '소스 선택 : 렌치드레싱'
            self.check.menuview.append(self.check.total_menu)

        # 세트 여부
        if setVal == 1: # 
            self.check.total_menu = '### 세트 ###'
            self.check.menuview.append(self.check.total_menu)
        elif setVal ==0:
            self.check.total_menu = '@@@ 단품 @@@'
            self.check.menuview.append(self.check.total_menu)

        self.check.show() # 두번째 창닫을 때까지 기다림
        self.close() # 두번째 창 닫으면 다시 첫번 째 창 보여짐
    
    def btnPrevClicked(self):
        obj = self.names[0]        
        self.names.pop()
        obj.show()
        self.close()
        
