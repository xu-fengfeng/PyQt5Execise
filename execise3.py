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
        pass
    
    #
    def move_event(self, value):
        print(value)
    
    def addButton(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        
        #dial.valueChanged.connect(self.move_event)
        dial.valueChanged.connect(lcd.display)
        
        slide = QSlider(self)
        slide.valueChanged.connect(lcd.display)
        
                  
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