import sys
import re
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QCheckBox, QLineEdit, QFormLayout, QBoxLayout, QTabWidget, QFrame, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Task2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 500)

        main_layout = QVBoxLayout()

        form = QFormLayout()

        name_layout = QHBoxLayout()
        self.surname = QLineEdit()
        self.surname.setPlaceholderText("Фамилия")
        self.name = QLineEdit()
        self.name.setPlaceholderText("Имя")
        self.patronymic = QLineEdit()
        self.patronymic.setPlaceholderText("Отчество")

        name_layout.addWidget(self.surname)
        name_layout.addWidget(self.name)
        name_layout.addWidget(self.patronymic)
        form.addRow("ФИО:", name_layout)

        self.email = QLineEdit()
        self.email.setPlaceholderText("email@example.com")
        form.addRow("Email:", self.email)

        self.phone = QLineEdit()
        self.phone.setPlaceholderText("+7XXXXXXXXXX")
        form.addRow("Телефон:", self.phone)

        themes_group = QGroupBox("Интересные темы")
        themes_layout = QVBoxLayout()

        self.theme1 = QCheckBox("Программирование")
        self.theme2 = QCheckBox("Дизайн")
        self.theme3 = QCheckBox("Маркетинг")
        self.theme4 = QCheckBox("Бизнес")

        themes_layout.addWidget(self.theme1)
        themes_layout.addWidget(self.theme2)
        themes_layout.addWidget(self.theme3)
        themes_layout.addWidget(self.theme4)
        themes_group.setLayout(themes_layout)

        form.addRow(themes_group)

        self.personal_check = QCheckBox("Согласие на обработку персональных данных *")
        self.news_check = QCheckBox("Согласие на рассылку")

        self.btn = QPushButton("Проверить")
        self.btn.clicked.connect(self.check)

        main_layout.addLayout(form)
        main_layout.addWidget(self.personal_check)
        main_layout.addWidget(self.news_check)
        main_layout.addWidget(self.btn)

        self.setLayout(main_layout)

    def check(self):
        errors = []

        if not self.surname.text():
            errors.append("Фамилия не заполнена")
        elif not re.match(r"[а-яA-Яa-zA-Z]+", self.surname.text()):
            errors.append("Фамилия задана не верно")
        if not self.name.text():
            errors.append("Имя не заполнено")
        elif not re.match(r"[а-яA-Яa-zA-Z]+", self.name.text()):
            errors.append("Имя задано не верно")
        if not self.patronymic.text():
            errors.append("Отчество не заполнено")
        elif not re.match(r"[а-яA-Яa-zA-Z]+", self.patronymic.text()):
            errors.append("Отчество задано не верно")

        email = self.email.text()
        if not email:
            errors.append("Email не заполнен")
        elif not re.match(r".+@.+\..+", email):  # Простейшая проверка email
            errors.append("Неверный формат email")

        phone = self.phone.text()
        if not phone:
            errors.append("Телефон не заполнен")
        elif not re.match(r"^(\+7|8)\d{10}$", phone):  # Хотя бы цифры и плюс
            errors.append("Телефон указан не верно")

        if not self.personal_check.isChecked():
            errors.append("Нет согласия на обработку данных")

        if errors:
            QMessageBox.warning(self, "Ошибка", "\n".join(errors))
        else:
            QMessageBox.information(self, "Успех", "Все данные заполнены верно!")
