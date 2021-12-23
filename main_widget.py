import sys
from os import path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout


from control_layout import ControlLayout
from main_picture import MainPicture


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)


class MainWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Программа для выбора параметров резьбы")
        self.setWindowIcon(QIcon(resource_path("icon.ico")))
        self.setFixedSize(1220, 800)
        self.setStyleSheet("background-color: white;")

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.mainLayout = QHBoxLayout(self.main_widget)

        self.controlLayout = ControlLayout()
        self.mainPicture = MainPicture()

        self.mainLayout.addWidget(self.mainPicture, 0)
        self.mainLayout.addLayout(self.controlLayout, 1)

        self.controlLayout.signal_changed.sigchr.connect(self.mainPicture.fillMainPicture)
