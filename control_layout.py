from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QComboBox, QLineEdit, QCompleter

from spreadsheet_widget import SpreadsheetWidget
from add_picture import AddPicture
from open_data import OpenData
from signal_changed import SignalChanged
from choose_closest import ChooseClosest


class ControlLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.openData = OpenData()
        self.threadData = []
        self.signal_changed = SignalChanged()

        self.initLegends()
        self.initUI()
        self.spreadsheet = SpreadsheetWidget()
        self.addPicture = AddPicture()
        self.chooseClosest = ChooseClosest()

        self.addWidget(self.line)
        self.addWidget(self.l_d)
        self.addWidget(self.combo_d)
        # ==========================
        self.addWidget(self.l_p)
        self.addWidget(self.combo_p)
        # ==========================
        self.addWidget(self.l_name)
        self.addWidget(self.line_name_for_copy)
        # ==========================
        self.addLayout(self.chooseClosest)
        # ==========================
        self.addWidget(self.addPicture)
        # ==========================
        self.addWidget(self.spreadsheet)

        self.combo_d.addItems(self.openData.getDiameter())

    def initLegends(self):
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.l_d = QLabel('Выберите номинальный диаметр резьбы:')
        self.l_d.setAlignment(Qt.AlignCenter)

        self.l_p = QLabel('Выберите шаг резьбы:')
        self.l_p.setAlignment(Qt.AlignCenter)

        self.l_name = QLabel('Обозначение резьбы:')
        self.l_name.setAlignment(Qt.AlignCenter)

    def initUI(self):
        self.combo_d = QComboBox()
        completer = QCompleter(self.openData.getDiameter())
        self.combo_d.setCompleter(completer)
        self.combo_d.setFixedSize(388, 32)
        self.combo_d.activated.connect(self.chooseDiameter)

        self.combo_p = QComboBox()
        self.combo_p.setFixedSize(388, 32)
        self.combo_p.activated.connect(self.chooseStep)

        self.line_name_for_copy = QLineEdit()
        self.line_name_for_copy.setFixedSize(388, 32)
        self.line_name_for_copy.setReadOnly(True)
        self.line_name_for_copy.setAlignment(Qt.AlignCenter)

    def chooseDiameter(self):
        self.combo_p.clear()
        self.combo_p.addItems(self.openData.getStep(self.combo_d.currentText()))
        self.chooseClosest.fillRows(self.openData.getClosest(self.combo_d.currentText()))
        self.chooseStep()

    def chooseStep(self):
        if self.combo_p.currentIndex() == 0:
            self.line_name_for_copy.setText('M' + str(self.combo_d.currentText()))
        else:
            self.line_name_for_copy.setText('M' + str(self.combo_d.currentText()) + 'x' + str(self.combo_p.currentText()))

        self.threadData = self.openData.getThreadData(self.combo_d.currentText(), self.combo_p.currentText())
        self.addPicture.fillAddPicture(self.threadData)
        self.spreadsheet.fillSpreadsheet(self.threadData)
        self.signal_changed.sigchr.emit(self.threadData)
