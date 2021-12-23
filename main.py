from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from ctypes import windll

from main_widget import MainWidget

myappid = 'mycompany.myproduct.subproduct.version'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == "__main__":
    qApp = QApplication(argv)

    aw = MainWidget()
    aw.showMaximized()
    exit(qApp.exec_())

