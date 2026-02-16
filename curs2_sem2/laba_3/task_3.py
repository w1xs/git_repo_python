import sys
from datetime import datetime, date
from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QPushButton, QVBoxLayout, QHBoxLayout,
                               QDateEdit, QTextEdit, QFrame)
from PySide6.QtCore import Qt, QDate


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор возраста")
        self.setGeometry(200, 200, 500, 400)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        top_frame = QFrame()
        top_frame.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        top_frame.setLineWidth(2)
        top_frame.setStyleSheet("padding: 10px;")

        top_layout = QVBoxLayout()

        title = QLabel("Введите вашу дату рождения")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd.MM.yyyy")
        self.date_edit.setDate(QDate(2000, 1, 1))

        current_date = QDate.currentDate()
        self.date_edit.setDateRange(QDate(1900, 1, 1), current_date)

        self.calc_button = QPushButton("Рассчитать")
        self.calc_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                padding: 8px;
                background-color: #3498db;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.calc_button.clicked.connect(self.calculate_age)

        top_layout.addWidget(title)
        top_layout.addWidget(self.date_edit)
        top_layout.addWidget(self.calc_button)
        top_frame.setLayout(top_layout)

        bottom_frame = QFrame()
        bottom_frame.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        bottom_frame.setLineWidth(2)
        bottom_frame.setStyleSheet("padding: 10px;")

        bottom_layout = QVBoxLayout()

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("""
            QTextEdit {
                font-family: Arial;
                font-size: 14px;
                background-color: white;
                color: black;
                border: 1px solid black;
            }
        """)

        self.result_text.setText("Введите дату рождения и нажмите 'Рассчитать'")

        bottom_layout.addWidget(self.result_text)
        bottom_frame.setLayout(bottom_layout)

        main_layout.addWidget(top_frame, stretch=2)
        main_layout.addWidget(bottom_frame, stretch=3)

        self.setLayout(main_layout)

    def calculate_age(self):
        birth_qdate = self.date_edit.date()
        birth_date = date(
            birth_qdate.year(),
            birth_qdate.month(),
            birth_qdate.day()
        )
        now = datetime.now()
        current_date = now.date()

        if birth_date > current_date:
            self.result_text.setText("Ошибка: дата рождения не может быть в будущем!")
            return

        age_years = current_date.year - birth_date.year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age_years -= 1
        days_diff = (current_date - birth_date).days
        age_hours = days_diff * 24 + now.hour

        age_seconds = age_hours * 3600 + now.minute * 60 + now.second

        result = f"""
        ДАТА РОЖДЕНИЯ: {birth_date.strftime('%d.%m.%Y')}

        ========= РЕЗУЛЬТАТЫ =========

        Вам {age_years} года/лет

        Это {age_hours} часа/ов

        Или {age_seconds} секунд/ы

        -----------------------------
        Расчет выполнен: {now.strftime('%d.%m.%Y %H:%M')}
        """

        self.result_text.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())