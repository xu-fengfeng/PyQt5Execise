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
    
    def btn_func(self):
        sender = self.sender()
        print("sender is ", sender.text())
        
        if sender.text() == "Name":
            text, ok = QInputDialog.getText(self, "Input Name", "Name:")
            if ok:
                self.name_label.setText(text)
            
        
    
    def SetupItems(self):
        self.name_label = QLabel("Name")
        self.name_button  = QPushButton("Name")
        self.name_button.clicked.connect(self.btn_func)
        
        self.age_label = QLabel("Age")
        self.age_button  = QPushButton("Age")
        self.age_button.clicked.connect(self.btn_func)
        
        self.sex_label = QLabel("Height")
        self.sex_button  = QPushButton("Height")
        self.sex_button.clicked.connect(self.btn_func)
        
        self.info_label = QLabel("Info")
        self.info_button  = QPushButton("Info")
        self.info_button.clicked.connect(self.btn_func)
    
        self.text_edit = QTextEdit()
    
    def SetupLayout(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.name_label, 0, 0, 1, 1)
        self.layout.addWidget(self.name_button, 0, 1, 1, 1)
    
        self.layout.addWidget(self.age_label, 1, 0, 1, 1)
        self.layout.addWidget(self.age_button, 1, 1, 1, 1)
        
        self.layout.addWidget(self.sex_label, 2, 0, 1, 1)
        self.layout.addWidget(self.sex_button, 2, 1, 1, 1)        
    
        self.layout.addWidget(self.info_label, 3, 0, 1, 1)
        self.layout.addWidget(self.info_button, 3, 1, 1, 1)
    
        self.layout.addWidget(self.text_edit, 4, 0, 0, 0)
    
        self.setLayout(self.layout)
    
    def SetupActions(self):
        self.openAction = QAction(self)
        self.openAction.setText("Open")
        self.openAction.setShortcut("Ctrl+Q")
        self.openAction.setStatusTip("open file")
        
        self.openAction.triggered.connect(self.openfunc)

        self.explorer_action = QAction(self)
        self.explorer_action.setText("Explorer")
        
        self.cmd_action = QAction("cmd", self)
    
        self.exit_action = QAction("&Exit", self)
        self.exit_action.setStatusTip("exit the program")
    
        self.new_action = QAction("New", self)
        
        self.save_action = QAction("Save", self)
    
    def SetupMenuAndBars(self):
        self.statusBar().showMessage("Ready")
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File(&F)")
        file_menu.addAction(self.openAction)
        
        openfolder_menu = QMenu("Open Containing Folder", self)

        openfolder_menu.addAction(self.explorer_action)
        openfolder_menu.addAction(self.cmd_action)
              
        file_menu.addMenu(openfolder_menu)
        
        file_menu.addAction(self.exit_action)
    
    def SetupToolBars(self):
        toolbar = self.addToolBar("ToolBar")
    
        
    def contextMenuEvent(self, event):
        cmenu = QMenu()
        cmenu.addAction(self.new_action)
        cmenu.addAction(self.save_action)
        
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action.text() == "New":
            print("New is clicked.")
    
    def SetupCenterWidget(self):
        widget = QWidget()
        widget.setLayout(self.layout) 
        self.setCentralWidget(widget)
                  
    def Setup(self):
        self.setGeometry(300, 300, 400, 300)
        self.addTitle()
        self.addIcon()
        self.addButton()
        self.SetupActions()
        self.SetupMenuAndBars()
        self.SetupToolBars()
        self.SetupItems()
        self.SetupLayout()
        self.SetupCenterWidget()
        
        self.show()
        
if __name__ == "__main__":
    print("program start..")
    print(PyQt5.__name__)
    
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    
    sys.exit(app.exec_())
    print("porgram finished.")        