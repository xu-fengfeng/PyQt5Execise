#coding=utf-8
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

import PyQt5

#class hiren

class MyWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.Setup()
    
    def addTitle(self):
        self.setWindowTitle("Test Program")
    
    def addIcon(self):
        icon = QIcon("shell.ico")
        self.setWindowIcon(icon)  
    
        
    def addButton(self):
        pass
                  
    def addLayout(self):
        btn1 = QPushButton("Test1", self)
        btn2 = QPushButton("Test2", self)
        btn3 = QPushButton("Test3", self)
    
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)        
        
        self.setLayout(vbox)
                      
                  
    def Setup(self):
        self.setGeometry(300, 300, 300, 100)
        self.addTitle()
        self.addIcon()
        self.addLayout()
        self.show()

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.Setup()
        self.show()
    
    def btn_click_func(self):
        sender = self.sender();
        self.lcd.display(sender.text())
        
    def Setup(self):
        gridlayout = QGridLayout()
    
        self.lcd = QLCDNumber(self)
        #                        行  列    占几行 占几列
        gridlayout.addWidget(self.lcd, 0, 0, 3, 0)
        gridlayout.setSpacing(10)
        names = ['Cls', 'Bc', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']
        '''
        x = 0
        for i in names:
            if i == '':
                x += 1
                continue            
            button = QPushButton(i, self)                      
            gridlayout.addWidget(button, x/4+3, x%4, 1, 1)
            button.clicked.connect(self.btn_click_func)
            x += 1
        '''
        positions = [(i,j) for i in range(4,9) for j in range(4,8)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            gridlayout.addWidget(button, *position)
            button.clicked.connect(self.btn_click_func)            
        self.setLayout(gridlayout)
        
if __name__ == "__main__":
    print("program start..")
    print(PyQt5.__name__)
    
    app = QApplication(sys.argv)
    #icn = MyWidget()
    mywidget = Calc()
    
    sys.exit(app.exec_())
    print("porgram finished.")        