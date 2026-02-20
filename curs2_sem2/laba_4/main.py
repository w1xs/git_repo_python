import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QGridLayout, QLineEdit, QRadioButton, QBoxLayout, QTabWidget)
from PySide6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 500)
        main_layout = QVBoxLayout()
        tabs = QTabWidget()
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
