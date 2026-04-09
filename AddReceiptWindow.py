from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel,
                             QDateEdit, QComboBox, QLineEdit, QTableWidget, QHeaderView)
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtGui, QtCore

class AddReceiptWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setup_layout()

    def initUI(self):
        # Add reciept
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.amount = QLineEdit() 
        self.description = QLineEdit() 

        self.btn_add = QPushButton("Add Expense")
        self.btn_delete = QPushButton("Delete")
        
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Description", "Amount"])
        header = self.table.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignAbsolute)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def setup_layout(self):
        layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        # Row 1
        row1.addWidget(QLabel("Date"))
        row1.addWidget(self.date_box)
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Amount"))
        row1.addWidget(self.amount)

        # Row 2
        row2.addWidget(QLabel("Description"))
        row2.addWidget(self.description)

        # Row 3
        row3.addWidget(self.btn_add)
        row3.addWidget(self.btn_delete)

        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)
        layout.addWidget(self.table)

        self.setLayout(layout)

