import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QGridLayout, QLineEdit, QRadioButton, QBoxLayout, QCheckBox
, QDoubleSpinBox, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 500)

        self.base_milk_price = 45
        self.base_apple_price = 20
        self.base_banana_price = 25
        self.base_rice_price = 10

        self.milk_price = self.base_milk_price
        self.apple_price = self.base_apple_price
        self.banana_price = self.base_banana_price
        self.rice_price = self.base_rice_price
        self.result = 0

        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        top_container = QWidget()
        bottom_layout = QGridLayout()
        bottom_container = QWidget()

        milk_layout = QVBoxLayout()
        milk_container = QFrame()
        milk_container.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        milk_container.setLineWidth(2)
        milk_container.setStyleSheet("padding: 5 px")
        milk_container.setMaximumSize(150, 250)
        self.milk_name = QLabel(f"Молоко 1 л.\nЦена: {self.milk_price}")
        self.milk_name.setStyleSheet("font-size: 20px")
        milk_middle_container = QWidget()
        milk_middle_layout = QHBoxLayout()
        milk_get_it_text = QLabel("Выбрать: ")
        milk_get_it_text.setStyleSheet("font-size: 20px")
        self.milk_checkbox = QCheckBox()
        self.milk_checkbox.toggled.connect(self.update_total_from_checkbox)
        milk_middle_layout.addWidget(milk_get_it_text)
        milk_middle_layout.addWidget(self.milk_checkbox)
        milk_middle_container.setLayout(milk_middle_layout)
        milk_count = QLabel("Количество:")
        milk_count.setStyleSheet("font-size: 20px")
        self.milk_spin = QDoubleSpinBox(decimals=0, singleStep=1.0, value=1)
        self.milk_spin.setRange(1, 30)
        self.milk_spin.valueChanged.connect(self.update_price_and_total)
        milk_spin_line = self.milk_spin.lineEdit()
        if milk_spin_line:
            milk_spin_line.setReadOnly(True)
        milk_layout.addWidget(self.milk_name)
        milk_layout.addWidget(milk_middle_container)
        milk_layout.addWidget(milk_count)
        milk_layout.addWidget(self.milk_spin)
        milk_container.setLayout(milk_layout)

        apple_layout = QVBoxLayout()
        apple_container = QFrame()
        apple_container.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        apple_container.setLineWidth(2)
        apple_container.setStyleSheet("padding: 5 px")
        apple_container.setMaximumSize(150, 250)
        self.apple_name = QLabel(f"Яблоки 1 кг.\nЦена: {self.apple_price}")
        self.apple_name.setStyleSheet("font-size: 20px")
        apple_middle_container = QWidget()
        apple_middle_layout = QHBoxLayout()
        apple_get_it_text = QLabel("Выбрать: ")
        apple_get_it_text.setStyleSheet("font-size: 20px")
        self.apple_checkbox = QCheckBox()
        self.apple_checkbox.toggled.connect(self.update_total_from_checkbox)
        apple_middle_layout.addWidget(apple_get_it_text)
        apple_middle_layout.addWidget(self.apple_checkbox)
        apple_middle_container.setLayout(apple_middle_layout)
        apple_count = QLabel("Количество:")
        apple_count.setStyleSheet("font-size: 20px")
        self.apple_spin = QDoubleSpinBox(decimals=0, singleStep=1.0, value=1)
        self.apple_spin.setRange(1, 30)
        self.apple_spin.valueChanged.connect(self.update_price_and_total)
        apple_spin_line = self.apple_spin.lineEdit()
        if apple_spin_line:
            apple_spin_line.setReadOnly(True)
        apple_layout.addWidget(self.apple_name)
        apple_layout.addWidget(apple_middle_container)
        apple_layout.addWidget(apple_count)
        apple_layout.addWidget(self.apple_spin)
        apple_container.setLayout(apple_layout)

        banana_layout = QVBoxLayout()
        banana_container = QFrame()
        banana_container.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        banana_container.setLineWidth(2)
        banana_container.setStyleSheet("padding: 5 px")
        banana_container.setMaximumSize(150, 250)
        self.banana_name = QLabel(f"Бананы 1 кг.\nЦена: {self.banana_price}")
        self.banana_name.setStyleSheet("font-size: 20px")
        banana_middle_container = QWidget()
        banana_middle_layout = QHBoxLayout()
        banana_get_it_text = QLabel("Выбрать: ")
        banana_get_it_text.setStyleSheet("font-size: 20px")
        self.banana_checkbox = QCheckBox()
        self.banana_checkbox.toggled.connect(self.update_total_from_checkbox)
        banana_middle_layout.addWidget(banana_get_it_text)
        banana_middle_layout.addWidget(self.banana_checkbox)
        banana_middle_container.setLayout(banana_middle_layout)
        banana_count = QLabel("Количество:")
        banana_count.setStyleSheet("font-size: 20px")
        self.banana_spin = QDoubleSpinBox(decimals=0, singleStep=1.0, value=1)
        self.banana_spin.setRange(1, 30)
        self.banana_spin.valueChanged.connect(self.update_price_and_total)
        banana_spin_line = self.banana_spin.lineEdit()
        if banana_spin_line:
            banana_spin_line.setReadOnly(True)
        banana_layout.addWidget(self.banana_name)
        banana_layout.addWidget(banana_middle_container)
        banana_layout.addWidget(banana_count)
        banana_layout.addWidget(self.banana_spin)
        banana_container.setLayout(banana_layout)

        rice_layout = QVBoxLayout()
        rice_container = QFrame()
        rice_container.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        rice_container.setLineWidth(2)
        rice_container.setStyleSheet("padding: 5 px")
        rice_container.setMaximumSize(150, 250)
        self.rice_name = QLabel(f"Рис 1 кг.\nЦена: {self.rice_price}")
        self.rice_name.setStyleSheet("font-size: 20px")
        rice_middle_container = QWidget()
        rice_middle_layout = QHBoxLayout()
        rice_get_it_text = QLabel("Выбрать: ")
        rice_get_it_text.setStyleSheet("font-size: 20px")
        self.rice_checkbox = QCheckBox()
        self.rice_checkbox.toggled.connect(self.update_total_from_checkbox)
        rice_middle_layout.addWidget(rice_get_it_text)
        rice_middle_layout.addWidget(self.rice_checkbox)
        rice_middle_container.setLayout(rice_middle_layout)
        rice_count = QLabel("Количество:")
        rice_count.setStyleSheet("font-size: 20px")
        self.rice_spin = QDoubleSpinBox(decimals=0, singleStep=1.0, value=1)
        self.rice_spin.setRange(1, 30)
        self.rice_spin.valueChanged.connect(self.update_price_and_total)
        rice_spin_line = self.rice_spin.lineEdit()
        if rice_spin_line:
            rice_spin_line.setReadOnly(True)
        rice_layout.addWidget(self.rice_name)
        rice_layout.addWidget(rice_middle_container)
        rice_layout.addWidget(rice_count)
        rice_layout.addWidget(self.rice_spin)
        rice_container.setLayout(rice_layout)


        self.result_label = QLabel(f"Итоговая цена: {self.result}")
        self.result_label.setStyleSheet("font-size: 32px")


        top_layout.addWidget(rice_container)
        top_layout.addWidget(banana_container)
        top_layout.addWidget(apple_container)
        top_layout.addWidget(milk_container)
        top_container.setLayout(top_layout)

        bottom_layout.addWidget(self.result_label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_container.setLayout(bottom_layout)

        main_layout.addWidget(top_container, stretch=3)
        main_layout.addWidget(bottom_container, stretch=1)
        self.setLayout(main_layout)

    def update_prices(self):
        self.milk_price = int(self.milk_spin.value() * self.base_milk_price)
        self.milk_name.setText(f"Молоко 1 л.\nЦена: {self.milk_price}")

        self.apple_price = int(self.apple_spin.value() * self.base_apple_price)
        self.apple_name.setText(f"Яблоки 1 кг.\nЦена: {self.apple_price}")

        self.banana_price = int(self.banana_spin.value() * self.base_banana_price)
        self.banana_name.setText(f"Бананы 1 кг.\nЦена: {self.banana_price}")

        self.rice_price = int(self.rice_spin.value() * self.base_rice_price)
        self.rice_name.setText(f"Рис 1 кг.\nЦена: {self.rice_price}")

    def recalc_total(self):
        self.result = 0

        if self.milk_checkbox.isChecked():
            self.result += self.milk_price
        if self.apple_checkbox.isChecked():
            self.result += self.apple_price
        if self.banana_checkbox.isChecked():
            self.result += self.banana_price
        if self.rice_checkbox.isChecked():
            self.result += self.rice_price

        self.result_label.setText(f"Итоговая цена: {self.result}")

    def update_price_and_total(self):
        self.update_prices()
        self.recalc_total()

    def update_total_from_checkbox(self):
        self.recalc_total()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())