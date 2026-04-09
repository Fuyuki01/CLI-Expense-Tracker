from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, 
                             QDateEdit, QComboBox, QLineEdit, QTableWidget)
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtGui, QtCore
import AddReceiptWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Expanse Tracker")

        self.setFixedSize(QSize(800, 600))
        self.setStyleSheet("background-color: #2E3440; color: #ECEFF4;")


        self.initUI()
        
        self.receipt_Window = AddReceiptWindow.AddReceiptWindow()
        self.setCentralWidget(self.receipt_Window)

        self.top_bar_buttons[0].clicked.connect(self.add_receipt_button)

    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.top_Bar = QHBoxLayout()

        
        self.titles = ['Add reciept', 'History', 'Summary']
        self.top_bar_buttons = [QPushButton(title) for title in self.titles]

        for button in self.top_bar_buttons:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #3776C9;
                    color: white;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #6191CE;
                }
                QPushButton:pressed {
                    background-color: #456FA6;
                }
            """)
            self.top_Bar.addWidget(button)

        self.mainLayout.addLayout(self.top_Bar)
        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setMenuWidget(self.widget)
    
    def add_receipt_button(self):
        self.setCentralWidget(self.receipt_Window)

# self.top_Bar.setSpacing(20)
# self.top_Bar.setContentsMargins(5, 20, 0, 500)