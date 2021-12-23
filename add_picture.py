import sys
from os import path

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QLineEdit


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)


class AddPicture(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.path = resource_path("thread_pic.png")
        self.initLines()
        self.initScene()

        self.setScene(self.scene)

    def initLines(self):
        self.line_dD = QLineEdit()
        self.line_dD.setGeometry(56, 49, 50, 20)
        self.line_dD.setReadOnly(True)
        self.line_dD.setAlignment(QtCore.Qt.AlignCenter)
        self.line_dD.setStyleSheet("background: white;")

        self.line_P = QLineEdit()
        self.line_P.setGeometry(205, 4, 50, 20)
        self.line_P.setReadOnly(True)
        self.line_P.setAlignment(QtCore.Qt.AlignCenter)
        self.line_P.setStyleSheet("background: white;")

        self.line_dD1 = QLineEdit()
        self.line_dD1.setGeometry(56, 133, 50, 20)
        self.line_dD1.setReadOnly(True)
        self.line_dD1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_dD1.setStyleSheet("background: white;")

        self.line_dD2 = QLineEdit()
        self.line_dD2.setGeometry(56, 99, 50, 20)
        self.line_dD2.setReadOnly(True)
        self.line_dD2.setAlignment(QtCore.Qt.AlignCenter)
        self.line_dD2.setStyleSheet("background: white;")

    def initScene(self):
        self.scene = QGraphicsScene(0, 0, 380, 250)

        pixmap = QPixmap(self.path)
        pixmap = pixmap.scaled(380, 250)
        self.scene.addPixmap(pixmap)

        self.scene.addWidget(self.line_dD)
        self.scene.addWidget(self.line_P)
        self.scene.addWidget(self.line_dD1)
        self.scene.addWidget(self.line_dD2)

    def fillAddPicture(self, threadData):
        self.line_dD.setText(str(threadData[0]))
        self.line_P.setText(str(threadData[1]))
        self.line_dD1.setText(str(threadData[2]))
        self.line_dD2.setText(str(threadData[3]))