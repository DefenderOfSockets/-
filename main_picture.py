import sys
from os import path

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QLineEdit


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)


class MainPicture(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.path = resource_path("thread_pic2.png")
        self.initLines()
        self.initScene()

        self.setScene(self.scene)

    def initScene(self):
        self.scene = QGraphicsScene(0, 0, 800, 750)

        pixmap = QPixmap(self.path)
        pixmap = pixmap.scaled(800, 750)
        self.scene.addPixmap(pixmap)

        self.scene.addWidget(self.line_shaft_d)
        self.scene.addWidget(self.line_shaft_x)
        self.scene.addWidget(self.line_shaft_z)
        self.scene.addWidget(self.line_shaft_a)
        self.scene.addWidget(self.line_shaft_df)
        self.scene.addWidget(self.line_shaft_f)
        self.scene.addWidget(self.line_shaft_r1)
        self.scene.addWidget(self.line_shaft_r)

        self.scene.addWidget(self.line_hole_d)
        self.scene.addWidget(self.line_hole_x)
        self.scene.addWidget(self.line_hole_z)
        self.scene.addWidget(self.line_hole_a)
        self.scene.addWidget(self.line_hole_df)
        self.scene.addWidget(self.line_hole_f)
        self.scene.addWidget(self.line_hole_r1)
        self.scene.addWidget(self.line_hole_r)

    def initLines(self):
        self.line_shaft_d = QLineEdit()
        self.line_shaft_d.setGeometry(335, 75, 60, 25)
        self.line_shaft_d.setReadOnly(True)
        self.line_shaft_d.setAlignment(QtCore.Qt.AlignCenter)
        self.line_shaft_d.setStyleSheet("background: white;")

        self.line_shaft_x = QLineEdit()
        self.line_shaft_x.setGeometry(120, 153, 60, 25)
        self.line_shaft_x.setReadOnly(True)
        self.line_shaft_x.setAlignment(QtCore.Qt.AlignCenter)
        self.line_shaft_x.setStyleSheet("background: white;")

        self.line_shaft_z = QLineEdit()
        self.line_shaft_z.setGeometry(305, 375, 60, 25)
        self.line_shaft_z.setReadOnly(True)
        self.line_shaft_z.setAlignment(QtCore.Qt.AlignCenter)
        self.line_shaft_z.setStyleSheet("background: white;")

        self.line_shaft_a = QLineEdit()
        self.line_shaft_a.setGeometry(120, 375, 60, 25)
        self.line_shaft_a.setReadOnly(True)
        self.line_shaft_a.setAlignment(QtCore.Qt.AlignCenter)
        self.line_shaft_a.setStyleSheet("background: white;")

        self.line_shaft_df = QLineEdit()
        self.line_shaft_df.setGeometry(155, 713, 60, 25)
        self.line_shaft_df.setReadOnly(True)
        self.line_shaft_df.setAlignment(QtCore.Qt.AlignCenter)
        self.line_shaft_df.setStyleSheet("background: white;")

        self.line_shaft_f = QLineEdit()
        self.line_shaft_f.setGeometry(55, 483, 60, 25)
        self.line_shaft_f.setReadOnly(True)
        self.line_shaft_f.setAlignment(QtCore.Qt.AlignCenter)
        self.line_shaft_f.setStyleSheet("background: white;")

        self.line_shaft_r1 = QLineEdit()
        self.line_shaft_r1.setGeometry(200, 483, 60, 25)
        self.line_shaft_r1.setReadOnly(True)
        self.line_shaft_r1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_shaft_r1.setStyleSheet("background: white;")

        self.line_shaft_r = QLineEdit()
        self.line_shaft_r.setGeometry(156, 663, 60, 25)
        self.line_shaft_r.setReadOnly(True)
        self.line_shaft_r.setAlignment(QtCore.Qt.AlignCenter)
        self.line_shaft_r.setStyleSheet("background: white;")

        self.line_hole_d = QLineEdit()
        self.line_hole_d.setGeometry(695, 75, 60, 25)
        self.line_hole_d.setReadOnly(True)
        self.line_hole_d.setAlignment(QtCore.Qt.AlignCenter)
        self.line_hole_d.setStyleSheet("background: white;")

        self.line_hole_x = QLineEdit()
        self.line_hole_x.setGeometry(425, 183, 60, 25)
        self.line_hole_x.setReadOnly(True)
        self.line_hole_x.setAlignment(QtCore.Qt.AlignCenter)
        self.line_hole_x.setStyleSheet("background: white;")

        self.line_hole_z = QLineEdit()
        self.line_hole_z.setGeometry(665, 387, 60, 25)
        self.line_hole_z.setReadOnly(True)
        self.line_hole_z.setAlignment(QtCore.Qt.AlignCenter)
        self.line_hole_z.setStyleSheet("background: white;")

        self.line_hole_a = QLineEdit()
        self.line_hole_a.setGeometry(530, 387, 60, 25)
        self.line_hole_a.setReadOnly(True)
        self.line_hole_a.setAlignment(QtCore.Qt.AlignCenter)
        self.line_hole_a.setStyleSheet("background: white;")

        self.line_hole_df = QLineEdit()
        self.line_hole_df.setGeometry(500, 698, 60, 25)
        self.line_hole_df.setReadOnly(True)
        self.line_hole_df.setAlignment(QtCore.Qt.AlignCenter)
        self.line_hole_df.setStyleSheet("background: white;")

        self.line_hole_f = QLineEdit()
        self.line_hole_f.setGeometry(590, 638, 60, 25)
        self.line_hole_f.setReadOnly(True)
        self.line_hole_f.setAlignment(QtCore.Qt.AlignCenter)
        self.line_hole_f.setStyleSheet("background: white;")

        self.line_hole_r = QLineEdit()
        self.line_hole_r.setGeometry(420, 442, 60, 25)
        self.line_hole_r.setReadOnly(True)
        self.line_hole_r.setAlignment(QtCore.Qt.AlignCenter)
        self.line_hole_r.setStyleSheet("background: white;")

        self.line_hole_r1 = QLineEdit()
        self.line_hole_r1.setGeometry(590, 440, 60, 25)
        self.line_hole_r1.setReadOnly(True)
        self.line_hole_r1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_hole_r1.setStyleSheet("background: white;")

    def fillMainPicture(self, threadData):
        self.line_shaft_d.setText(threadData[0])
        self.line_hole_d.setText(threadData[0])

        self.line_shaft_x.setText(threadData[5])
        self.line_shaft_a.setText(threadData[6])
        self.line_shaft_f.setText(threadData[7])
        self.line_shaft_r.setText(threadData[8])
        self.line_shaft_r1.setText(threadData[9])
        self.line_shaft_df.setText(threadData[10])
        self.line_shaft_z.setText(threadData[4])

        self.line_hole_x.setText(threadData[11])
        self.line_hole_a.setText(threadData[12])
        self.line_hole_f.setText(threadData[13])
        self.line_hole_r.setText(threadData[14])
        self.line_hole_r1.setText(threadData[15])
        self.line_hole_df.setText(threadData[16])
        self.line_hole_z.setText(threadData[4])
