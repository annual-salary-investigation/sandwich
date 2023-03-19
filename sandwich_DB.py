# 샌드위치 키오스크 앱
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
import pymysql
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
        self.conn = pymysql.connect(host='210.119.12.72', user='root', password='12345',
                                    db='sandwich2', charset='utf8')
        print(self.sender().objectName())
        menuName = self.sender().objectName()


        if menuName == 'btnmenu1': # 이탈리안 비엠티
            menuVal = 4
        elif menuName == 'btnmenu2': # 에그마요
            menuVal = 3
        elif menuName == 'btnmenu3': # 스테이크 & 치즈
            menuVal = 2
        elif menuName == 'btnmenu4': # 서브웨이 클럽
            menuVal = 1
        elif menuName == 'btnmenu5': # 치킨 데리야끼
            menuVal = 5

        query = '''INSERT INTO orders
                        (ProNo
                       , TakeOut
                       , SetYn
                       , OrderDt
                       , CreditCardYn)
                    VALUES
                        (%s,
                        NULL,
                        NULL,
                        now(),
                        1)
                '''
        cur = self.conn.cursor()
        cur.execute(query, (menuVal))
        self.conn.commit()
        self.conn.close()

        print('메뉴 저장')
        
        self.hide() # 메인 윈도우 숨김
        self.second = Bread()      
        self.second.names.append(self)
        self.second.exec() # 두번째 창닫을 때까지 기다림        
        self.show() # 두번째 창 닫으면 다시 첫번 째 창 보여짐
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())        

    