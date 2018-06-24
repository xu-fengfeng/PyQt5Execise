#coding=utf-8
'''
Created on 2018年6月24日

@author: xufengfeng
'''

import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

import PyQt5

class MyWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.Setup()
    def addTitle(self):
        self.setWindowTitle("Test Program")
    def addIcon(self):
        icon = QIcon("shell.ico")
        self.setWindowIcon(icon)  
    
    def SetupLayout(self):
        formlayout = QFormLayout()
        
        label1 = QLabel("label1")
        label2 = QLabel("label2")
        
        lineedit1 = QLineEdit()
        lineedit2 = QLineEdit()
        
        formlayout.addRow(label1, lineedit1)
        formlayout.addRow(label2, lineedit2)
        
        self.setLayout(formlayout)
        
    def addButton(self):
        pass
                  
    def Setup(self):
        self.addTitle()
        self.addIcon()
        self.addButton()
        self.SetupLayout()
        self.show()
        
if __name__ == "__main__":
    print("program start..")
    print(PyQt5.__name__)
    
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    
    sys.exit(app.exec_())
    print("porgram finished.") 