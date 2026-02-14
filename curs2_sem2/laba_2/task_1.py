import sys
from PIL.ImageQt import QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)

        main_layout = QVBoxLayout()
        self.text_label = QLabel("Отпущена")
        self.text_label.setStyleSheet("font-size:22px")
        self.button = QPushButton("КНОПКА")
        self.button.setMinimumSize(150, 40)
        self.button.setMaximumSize(300,80)
        self.button.pressed.connect(self.button_is_down)
        self.button.released.connect(self.button_is_up)
        main_layout.addWidget(self.text_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(main_layout)

    def button_is_down(self):
        self.text_label.setText("Нажата")

    def button_is_up(self):
        self.text_label.setText("Отпущена")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())