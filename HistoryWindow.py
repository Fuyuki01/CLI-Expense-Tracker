from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QDialog, QTableWidget, QHeaderView
from PyQt5.QtCore import QSize, Qt, QDate

class HistoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setup_Layout()
    
    def initUI(self):
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Description", "Amount"])
        header = self.table.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignAbsolute)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def setup_Layout(self):
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.table)
        self.setLayout(mainLayout)