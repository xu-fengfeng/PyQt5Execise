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
    
    def about_function(self):
        print("Message Box")
        QMessageBox.about(self, "about the project", "about the project")
        QMessageBox.aboutQt(self)
        
    def addButton(self):
        about_button = QPushButton("关于", self)  #创造一个pushbutton，父窗口是这个类实例
        about_button.setGeometry(0, 0, 70 ,30)
        about_button.clicked.connect(self.about_function)
        
        textline = QLineEdit(self)
        textline.setGeometry(0, 30, 70, 30)
        
        
        
                  
    def Setup(self):
        self.setGeometry(300, 300, 300, 100)
        self.addTitle()
        self.addIcon()
        self.addButton()
        self.show()
        
if __name__ == "__main__":
    print("program start..")
    print(PyQt5.__name__)
    
    app = QApplication(sys.argv)
    icn = MyWidget()
    
    sys.exit(app.exec_())
    print("porgram finished.")        