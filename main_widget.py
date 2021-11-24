from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from control_layout import ControlLayout
from main_picture import MainPicture


class MainWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Программа для выбора параметров резьбы")
        self.setWindowIcon(QIcon('pic/icon.png'))
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
