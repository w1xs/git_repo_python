import sys
from PIL.ImageQt import QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.setGeometry(200,200,500,500)

        main_layout = QVBoxLayout()
        self.count_label = QLabel(str(self.count), self)
        self.count_label.setStyleSheet("font-size: 30px")

        bottom_layout = QHBoxLayout()
        count_up_button = QPushButton("+1")
        count_up_button.setStyleSheet("font-size: 20px")
        count_up_button.clicked.connect(self.count_up)
        count_up_button.setMinimumSize(150,80)
        count_down_button = QPushButton("C")
        count_down_button.setStyleSheet("font-size: 20px")
        count_down_button.clicked.connect(self.count_down)
        count_down_button.setMinimumSize(150,80)
        bottom_layout.addWidget(count_down_button,alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_layout.addWidget(count_up_button,alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.count_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)

    def count_up(self):
        self.count += 1
        self.count_label.setText(str(self.count))

    def count_down(self):
        self.count = 0
        self.count_label.setText(str(self.count))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())