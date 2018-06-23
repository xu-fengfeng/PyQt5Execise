import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import *

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
    def Setup(self):
        self.addTitle()
        self.addIcon()
        self.show()
        
if __name__ == "__main__":
    print("program start..")
    app = QApplication(sys.argv)
    icn = MyWidget()
    
    sys.exit(app.exec_())
    print("porgram finished.")        