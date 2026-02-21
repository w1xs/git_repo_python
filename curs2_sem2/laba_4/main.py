import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QGridLayout, QLineEdit, QRadioButton, QBoxLayout, QTabWidget)
from PySide6.QtCore import Qt
from task_1 import Task1Window
from task_2 import Task2Window
from task_3 import Task3Window

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 500)
        main_layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(Task1Window(), "Задание 1")
        tabs.addTab(Task2Window(), "Задание 2")
        tabs.addTab(Task3Window(), "Задание 3")
        main_layout.addWidget(tabs)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
