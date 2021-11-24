import sys
from PyQt5.QtWidgets import QApplication
import ctypes
from main_widget import MainWidget

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == "__main__":
    qApp = QApplication(sys.argv)

    aw = MainWidget()
    aw.showMaximized()
    sys.exit(qApp.exec_())
