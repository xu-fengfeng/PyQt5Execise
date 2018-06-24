#coding=utf-8
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

import PyQt5

#class hiren
class MySignalClass(QObject):
    #def __init__(self):
    print("self.mysignal is inited.")
    mysignal = pyqtSignal()


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
    
    def clickfunc(self, event):
        print("button is clicked")
    
    def keyPressEvent(self, e):
        #print("key %s is clicked"%e.key())
        if e.key() == Qt.Key_Up:
            print("key ↑ is clicked")
    
    def mouseMoveEvent(self, event):
        print(event.x(), event.y())
        self.pos = event.pos()
        self.lab.setText("%d-%d"%(self.pos.x(),self.pos.y()))
        #self.update()
        return
    
    def paintEvent(self, event):
        if self.pos :
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())
        
    def btn_func(self):
        sender = self.sender()
        print("sender's name is ", sender.text())
        self.mysig.mysignal.emit()
        
    
    def addButton(self):
        self.lab = QLabel(self)
        self.lab.setText("abc")
        
        '''
        lcd = QLCDNumber(self)
        dial = QDial(self)
        
        #dial.valueChanged.connect(self.move_event)
        dial.valueChanged.connect(lcd.display)
        
        slide = QSlider(self)
        slide.valueChanged.connect(lcd.display)
        
        button = QPushButton("direction", self)
        button.setGeometry(0, 100, 80, 30)
        button.clicked.connect(self.clickfunc)
        '''
        btn = QPushButton("Test1", self)
        btn.clicked.connect(self.btn_func)
        btn.setGeometry(0, 0, 20, 20)
        
        btn2 = QPushButton("Test2", self)
        btn2.clicked.connect(self.btn_func)
        btn.setGeometry(20, 0, 20, 50)
    
    def mysig_func(self):
        print("mysig_func is called.")
    
    def SetupSignal(self):
        self.mysig = MySignalClass()    
        #self.mysig.mysignal.connect(self.mysig_func)
        self.mysig.mysignal.      
    def Setup(self):
        self.pos = None
        
        self.setGeometry(300, 300, 300, 350)
        self.addTitle()
        self.addIcon()
        self.addButton()
        self.SetupSignal()
        
        
        self.show()
        
        
        
if __name__ == "__main__":
    print("program start..")
    print(PyQt5.__name__)
    
    app = QApplication(sys.argv)
    icn = MyWidget()
    
    sys.exit(app.exec_())
    print("porgram finished.") 