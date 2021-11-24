from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem


class SpreadsheetWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.threadDataNames = ['d, D', 'P', 'd1, D1', 'd2, D2', 'z', 'x_вал', 'a_вал', 'f_вал', 'R_вал', 'R1_вал',
                                'df_вал',
                                'x_отв', 'a_отв', 'f_отв', 'R_отв', 'R1_отв', 'df_отв']

        self.setColumnCount(2)
        self.setRowCount(len(self.threadDataNames))
        self.setFixedSize(388, 250)

        # Устанавливаем заголовки таблицы
        self.setHorizontalHeaderLabels(["Параметр", "Значение, мм"])
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        # Заполняем первую строку
        for i in range(len(self.threadDataNames)):
            self.setItem(i, 0, QTableWidgetItem(str(self.threadDataNames[i])))

        # делаем ресайз колонок по содержимому
        self.resizeRowsToContents()

    def fillSpreadsheet(self, threadData):
        for i in range(len(threadData)):
            self.setItem(i, 1, QTableWidgetItem(str(threadData[i])))
