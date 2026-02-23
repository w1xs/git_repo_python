import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QTextEdit, QLineEdit, QFormLayout, QBoxLayout, QListView, QFrame, QMessageBox,
                               QDialog, QCheckBox, QGridLayout, QWizard, QWizardPage)
from PySide6.QtCore import Qt, QPoint, QAbstractListModel, QModelIndex
from PySide6.QtGui import QDrag, QPixmap, QAction



class LoginPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Входные данные")

        layout = QVBoxLayout()

        self.login_label = QLabel("Логин:")
        self.login_label.setStyleSheet("font-size: 20px;")
        self.login_edit = QLineEdit()
        self.login_edit.setStyleSheet("font-size: 20px;")

        self.password_label = QLabel("Пароль:")
        self.password_label.setStyleSheet("font-size: 20px;")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.setStyleSheet("font-size: 20px;")

        layout.addWidget(self.login_label)
        layout.addWidget(self.login_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)

        self.setLayout(layout)

        self.registerField("login*", self.login_edit)
        self.registerField("password*", self.password_edit)


class NamePage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Личные данные")

        layout = QVBoxLayout()

        self.surname_label = QLabel("Фамилия:")
        self.surname_label.setStyleSheet("font-size: 20px;")
        self.surname_edit = QLineEdit()
        self.surname_edit.setStyleSheet("font-size: 20px;")

        self.name_label = QLabel("Имя:")
        self.name_label.setStyleSheet("font-size: 20px;")
        self.name_edit = QLineEdit()
        self.name_edit.setStyleSheet("font-size: 20px;")

        self.patronymic_label = QLabel("Отчество:")
        self.patronymic_label.setStyleSheet("font-size: 20px;")
        self.patronymic_edit = QLineEdit()
        self.patronymic_edit.setStyleSheet("font-size: 20px;")

        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_edit)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.patronymic_label)
        layout.addWidget(self.patronymic_edit)

        self.setLayout(layout)

        self.registerField("surname*", self.surname_edit)
        self.registerField("name*", self.name_edit)
        self.registerField("patronymic", self.patronymic_edit)


class InterestsPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Интересы")

        layout = QVBoxLayout()

        themes_group = QGroupBox("Интересные темы")
        themes_group.setStyleSheet("font-size: 20px;")
        themes_layout = QVBoxLayout()

        self.theme1 = QCheckBox("Программирование")
        self.theme1.setStyleSheet("font-size: 20px;")
        self.theme2 = QCheckBox("Дизайн")
        self.theme2.setStyleSheet("font-size: 20px;")
        self.theme3 = QCheckBox("Маркетинг")
        self.theme3.setStyleSheet("font-size: 20px;")
        self.theme4 = QCheckBox("Бизнес")
        self.theme4.setStyleSheet("font-size: 20px;")


        themes_layout.addWidget(self.theme1)
        themes_layout.addWidget(self.theme2)
        themes_layout.addWidget(self.theme3)
        themes_layout.addWidget(self.theme4)
        themes_group.setLayout(themes_layout)

        self.news_check = QCheckBox("Согласие на рассылку")
        self.news_check.setStyleSheet("font-size: 20px;")

        layout.addWidget(themes_group)
        layout.addWidget(self.news_check)

        self.setLayout(layout)

        self.registerField("theme1", self.theme1)
        self.registerField("theme2", self.theme2)
        self.registerField("theme3", self.theme3)
        self.registerField("theme4", self.theme4)
        self.registerField("newsletter", self.news_check)


class RegistrationWizard(QWizard):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация пользователя")
        self.setStyleSheet("font-size: 20px;")

        self.addPage(LoginPage())
        self.addPage(NamePage())
        self.addPage(InterestsPage())


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.setGeometry(100, 100, 600, 500)

        layout = QVBoxLayout()

        self.register_button = QPushButton("Регистрация")
        self.register_button.setStyleSheet("font-size: 20px;")
        self.register_button.clicked.connect(self.open_wizard)

        self.info_display = QTextEdit()
        self.info_display.setStyleSheet("font-size: 20px;")
        self.info_display.setReadOnly(True)

        layout.addWidget(self.register_button)
        layout.addWidget(self.info_display)

        self.setLayout(layout)

    def open_wizard(self):
        wizard = RegistrationWizard()

        if wizard.exec() == QWizard.DialogCode.Accepted:
            themes = []
            if wizard.field("theme1"): themes.append("Футбол")
            if wizard.field("theme2"): themes.append("Баскетбол")
            if wizard.field("theme3"): themes.append("Волейбол")
            if wizard.field("theme4"): themes.append("Теннис")

            themes_text = ", ".join(themes) if themes else "не выбраны"
            newsletter_text = "Да" if wizard.field("newsletter") else "Нет"

            info = f"""
            ДАННЫЕ ПОЛЬЗОВАТЕЛЯ
            ==================
            Логин: {wizard.field("login")}
            ФИО: {wizard.field("surname")} {wizard.field("name")} {wizard.field("patronymic")}
            Интересные темы: {themes_text}
            Рассылка: {newsletter_text}
            """

            self.info_display.setText(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())