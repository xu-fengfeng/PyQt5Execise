import os
import sys


from PyQt5.QtWidgets import QWidget, QApplication




if __name__ == "__main__":
    print("program start..")
    app =QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Test Program")
    w.resize(250, 150)
    w.move(300, 300)
    w.show()
    sys.exit(app.exec_())
    
    
    print("porgram finished.")
