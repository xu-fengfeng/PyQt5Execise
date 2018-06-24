#coding=utf-8
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

import PyQt5

class MyWidget(QMainWindow):
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
    
    def openfunc(self):
        print("Open")
    
    def SetupActions(self):
        self.openAction = QAction(self)
        self.openAction.setText("Open")
        self.openAction.triggered.connect(self.openfunc)
    
    def SetupMenuAndBars(self):
        self.statusBar().showMessage("Ready")
        menubar = self.menuBar()
        menu = menubar.addMenu("File")
        menu.addAction(self.openAction)
        
                  
    def Setup(self):
        self.addTitle()
        self.addIcon()
        self.addButton()
        self.SetupActions()
        self.SetupMenuAndBars()
        self.show()
        
if __name__ == "__main__":
    print("program start..")
    print(PyQt5.__name__)
    
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    
    sys.exit(app.exec_())
    print("porgram finished.")        