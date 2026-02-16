import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QGridLayout, QLineEdit, QRadioButton, QBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from plotly.graph_objs import Layout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 500)
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        top_container = QWidget()
        bottom_layout = QGridLayout()
        bottom_container = QWidget()

        self.winter_button = QRadioButton("Зима")
        self.winter_button.setStyleSheet("font-size: 20px; border: 2px solid black; margin: 3px")
        self.winter_button.toggled.connect(self.choice)
        self.spring_button = QRadioButton("Весна")
        self.spring_button.setStyleSheet("font-size: 20px; border: 2px solid black; margin: 3px")
        self.spring_button.toggled.connect(self.choice)
        self.autumn_button = QRadioButton("Осень")
        self.autumn_button.setStyleSheet("font-size: 20px; border: 2px solid black; margin: 3px")
        self.autumn_button.toggled.connect(self.choice)
        self.summer_button = QRadioButton("Лето")
        self.summer_button.setStyleSheet("font-size: 20px; border: 2px solid black; margin: 3px")
        self.summer_button.toggled.connect(self.choice)

        top_layout.addWidget(self.winter_button)
        top_layout.addWidget(self.spring_button)
        top_layout.addWidget(self.summer_button)
        top_layout.addWidget(self.autumn_button)

        field = QLabel()
        field.setMinimumSize(600,250)
        field.setStyleSheet("border: 2px solid black")
        header = QLabel("Информация:")
        header.setStyleSheet("font-size: 20px; padding: 5px")
        self.info = QLabel()
        self.info.setStyleSheet("font-size: 20px; padding: 5px")
        self.winter_button.toggle()
        self.info.setText("Сухо, холодно и мало солнца")

        bottom_layout.addWidget(field, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_layout.addWidget(header, 0, 0, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        bottom_layout.addWidget(self.info, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)

        bottom_container.setLayout(bottom_layout)
        top_container.setLayout(top_layout)
        main_layout.addWidget(top_container)
        main_layout.addWidget(bottom_container)
        self.setLayout(main_layout)

    def choice(self):
        if self.winter_button.isChecked():
            self.info.setText("Сухо, холодно и мало солнца")
        elif self.spring_button.isChecked():
            self.info.setText("Влажно, тепло и средне солнца")
        elif self.summer_button.isChecked():
            self.info.setText("Сухо, жарко и много солнца")
        elif self.autumn_button.isChecked():
            self.info.setText("Влажно, прохладно и средне солнца")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
