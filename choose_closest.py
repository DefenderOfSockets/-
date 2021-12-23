from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel


class ChooseClosest(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.initLegends()
        self.initRows()

        self.addLayout(self.row_first)
        self.addLayout(self.row_second)
        self.addLayout(self.row_third)

    def initLegends(self):
        self.l_row = QLabel('Ряд резьбы: ')
        self.l_cl1 = QLabel('Ближайший диаметр по 1 ряду: ')
        self.l_cl2 = QLabel('Ближайший диаметр по 2 ряду: ')

        self.l_row_res = QLabel()
        self.l_row_res.setAlignment(Qt.AlignCenter)
        self.l_cl1_res = QLabel()
        self.l_cl1_res.setAlignment(Qt.AlignCenter)
        self.l_cl2_res = QLabel()
        self.l_cl2_res.setAlignment(Qt.AlignCenter)

    def initRows(self):
        self.row_first = QHBoxLayout()
        self.row_first.addWidget(self.l_row)
        self.row_first.addWidget(self.l_row_res)

        self.row_second = QHBoxLayout()
        self.row_second.addWidget(self.l_cl1)
        self.row_second.addWidget(self.l_cl1_res)

        self.row_third = QHBoxLayout()
        self.row_third.addWidget(self.l_cl2)
        self.row_third.addWidget(self.l_cl2_res)

    def fillRows(self, closest):
        self.l_row_res.clear()
        self.l_cl1_res.clear()
        self.l_cl2_res.clear()

        if closest[0] == '1':
            self.l_row_res.setText(closest[0])
            self.l_cl1_res.setText(closest[1])
        elif closest[0] == '2':
            self.l_row_res.setText(closest[0])
            self.l_cl1_res.setText(closest[2] + ', ' + closest[3])
            self.l_cl2_res.setText(closest[1])
        else:
            self.l_row_res.setText(closest[0])
            self.l_cl1_res.setText(closest[2] + ', ' + closest[3])
            self.l_cl2_res.setText(closest[4] + ', ' + closest[5])
