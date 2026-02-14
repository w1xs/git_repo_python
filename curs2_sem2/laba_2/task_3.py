import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QGridLayout, QLineEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont



class Window(QWidget):
    def __init__(self):
        self.value_1 = 0
        self.value_2 = 0
        self.result = 0
        self.calculation_string = "Введите данные"
        self.error = False
        super().__init__()
        self.setGeometry(200, 200, 400, 500)
        main_layout = QVBoxLayout()
        bottom_layout = QHBoxLayout()
        bottom_container = QWidget()
        left_bottom_layout = QVBoxLayout()
        left_bottom_container = QWidget()
        left_bottom_container.setStyleSheet("border: 2px solid black")
        right_bottom_layout = QGridLayout()
        right_bottom_container = QWidget()
        right_bottom_container.setStyleSheet("border: 2px solid black")

        self.result_label = QLabel(self.calculation_string)
        self.result_label.setStyleSheet("font-size: 40px")

        field_1_info = QLabel("Введите первое целое число")
        field_1_info.setStyleSheet("font-size: 15px")
        field_1_info.setMargin(10)
        self.field_1 = QLineEdit()
        self.field_1.setStyleSheet("font-size: 15px")
        field_2_info = QLabel("Введите второе целое число")
        field_2_info.setStyleSheet("font-size: 15px")
        field_2_info.setMargin(10)
        self.field_2 = QLineEdit()
        self.field_2.setStyleSheet("font-size: 15px")
        left_bottom_layout.addWidget(field_1_info)
        left_bottom_layout.addWidget(self.field_1)
        left_bottom_layout.addWidget(field_2_info)
        left_bottom_layout.addWidget(self.field_2)

        self.plus_button = QPushButton("+")
        self.plus_button.setMinimumSize(50,90)
        self.plus_button.setStyleSheet("font-size: 20px")
        self.plus_button.clicked.connect(self.plus)
        self.minus_button = QPushButton("-")
        self.minus_button.setMinimumSize(50,90)
        self.minus_button.setStyleSheet("font-size: 20px")
        self.minus_button.clicked.connect(self.minus)
        self.divide_button = QPushButton("/")
        self.divide_button.setMinimumSize(50,90)
        self.divide_button.setStyleSheet("font-size: 20px")
        self.divide_button.clicked.connect(self.divide)
        self.multiply_button = QPushButton("x")
        self.multiply_button.setMinimumSize(50,90)
        self.multiply_button.setStyleSheet("font-size: 20px")
        self.multiply_button.clicked.connect(self.multiply)
        self.exp_button = QPushButton("^")
        self.exp_button.setMinimumSize(50,90)
        self.exp_button.setStyleSheet("font-size: 20px")
        self.exp_button.clicked.connect(self.exp)
        self.equal_button = QPushButton("=")
        self.equal_button.setMinimumSize(50,90)
        self.equal_button.setStyleSheet("font-size: 20px")
        self.equal_button.clicked.connect(self.equal)

        right_bottom_layout.addWidget(self.plus_button, 0, 0,)
        right_bottom_layout.addWidget(self.minus_button, 1, 0)
        right_bottom_layout.addWidget(self.multiply_button, 0, 1)
        right_bottom_layout.addWidget(self.divide_button, 1, 1)
        right_bottom_layout.addWidget(self.exp_button, 0, 2)
        right_bottom_layout.addWidget(self.equal_button, 1, 2)

        left_bottom_container.setLayout(left_bottom_layout)
        bottom_layout.addWidget(left_bottom_container, alignment=Qt.AlignmentFlag.AlignCenter)
        right_bottom_container.setLayout(right_bottom_layout)
        bottom_layout.addWidget(right_bottom_container, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_container.setLayout(bottom_layout)
        main_layout.addWidget(self.result_label, alignment=Qt.AlignmentFlag.AlignCenter, stretch=1)
        main_layout.addWidget(bottom_container, alignment=Qt.AlignmentFlag.AlignCenter, stretch=2)
        self.setLayout(main_layout)

    def get_data(self):
        self.error = False
        text_1 = self.field_1.text()
        text_2 = self.field_2.text()
        if text_1 is None:
            self.field_1.setText("Введите целое число")
            self.result_label.setText("Error: Ошибка ввода")
            self.error = True
        else:
            if text_2 is None:
                self.field_2.setText("Введите целое число")
                self.result_label.setText("Error: Ошибка ввода")
                self.error = True
            else:
                try:
                    self.value_1 = int(text_1)
                except ValueError:
                    self.field_1.setText("Введите целое число")
                    self.result_label.setText("Error: Ошибка ввода")
                    self.error = True
                try:
                    self.value_2 = int(text_2)
                except ValueError:
                    self.field_2.setText("Введите целое число")
                    self.result_label.setText("Error: Ошибка ввода")
                    self.error = True

    def plus(self):
        self.get_data()
        if not self.error:
            self.result = self.value_1 + self.value_2
            self.calculation_string = f"{self.value_1} + {self.value_2}"
            self.result_label.setText(self.calculation_string)

    def minus(self):
        self.get_data()
        if not self.error:
            self.result = self.value_1 - self.value_2
            self.calculation_string = f"{self.value_1} - {self.value_2}"
            self.result_label.setText(self.calculation_string)

    def multiply(self):
        self.get_data()
        if not self.error:
            self.result = self.value_1 * self.value_2
            self.calculation_string = f"{self.value_1} * {self.value_2}"
            self.result_label.setText(self.calculation_string)

    def divide(self):
        self.get_data()
        if not self.error:
            if self.value_2 == 0 :
                self.result_label.setText("Error: Деление на 0")
                self.field_2.setText("Введите целое число")
            else:
                self.result = self.value_1 / self.value_2
                self.calculation_string = f"{self.value_1} / {self.value_2}"
                self.result_label.setText(self.calculation_string)

    def exp(self):
        self.get_data()
        if not self.error:
            self.result = self.value_1 ** self.value_2
            self.calculation_string = f"{self.value_1}^{self.value_2}"
            self.result_label.setText(self.calculation_string)

    def equal(self):
        if "=" not in self.calculation_string and not self.error:
            if self.value_1 is not None and self.value_2 is not None:
                self.calculation_string = self.calculation_string + f" = {self.result}"
                self.result_label.setText(self.calculation_string)
            else:
                self.result_label.setText("Введите данные")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
