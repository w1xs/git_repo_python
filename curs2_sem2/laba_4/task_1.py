import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QGridLayout, QLineEdit, QRadioButton, QBoxLayout, QTabWidget, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Task1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 1100, 1000)
        font = QFont()
        font.setPointSize(12)
        text_1 = ""
        text_2 = ""

        main_grid = QGridLayout()
        main_grid.setSpacing(0)
        main_grid.setContentsMargins(0, 0, 0, 0)

        text_1 = "пара\nвремя"
        self.add_cell(main_grid, text_1, font, 0, 0)
        text_1 = "ИТ-21БО"
        self.add_cell(main_grid, text_1, font, 0, 1, 1, 2)
        text_1 = "ИТ-22БО"
        self.add_cell(main_grid, text_1, font, 0, 3, 1, 2)
        text_1 = "ПОНЕДЕЛЬНИК"
        self.add_cell(main_grid, text_1, font, 1, 0, 1, 5)
        text_1 = "1\n9:00-\n10:35"
        self.add_cell(main_grid, text_1, font, 2, 0)
        text_1 = "Теория вероятностей\nи\nматематическая статистика\nСедов А.Г.\nауд.214"
        self.add_cell(main_grid, text_1, font, 2, 1, 1, 2)
        text_1 = "Компьютерные сети\nКоновалов Е.В\nауд. 224"
        self.add_cell(main_grid, text_1, font, 2, 3, 1, 2)
        text_1 = "2\n10:45-\n12:20"
        self.add_cell(main_grid, text_1, font, 3, 0)
        text_1 = "Компьютерные сети\nКоновалов Е.В\nауд. 224"
        text_2 = "Алгоритмы и анализ сложности\nТимофеев Е.А.\nауд. 215"
        self.add_vertical_split_cell(main_grid, text_1, text_2, font, 3, 1, 1, 4)
        text_1 = "3\n13:20-\n14:55"
        self.add_cell(main_grid, text_1, font, 4, 0)
        text_1 = "Компьютерные сети\nКоновалов Е.В\nауд. 224"
        self.add_cell(main_grid, text_1, font, 4, 1, 1, 2)
        text_1 = "Иностранный язык\nМоскалева Н.В.\nауд. 306"
        self.add_cell(main_grid, text_1, font, 4, 3, 1, 2)
        text_1 = "4\n15:05-\n16:40"
        self.add_cell(main_grid, text_1, font, 5, 0)
        text_1 = "Иностранный язык\nМастакова Н.К.\nауд. 305"
        self.add_cell(main_grid, text_1, font, 5, 1, 1, 2)
        text_1 = "Теория вероятностей\nи\nматематическая статистика\nСедов А.Г.\nауд.214"
        self.add_cell(main_grid, text_1, font, 5, 3, 1, 2)
        text_1 = "5\n16:50-\n18:25"
        self.add_cell(main_grid, text_1, font, 6, 0)
        text_1 = "\n\n\n"
        self.add_cell(main_grid, text_1, font, 6, 1, 1, 2)
        text_1 = "\n\n\n"
        self.add_cell(main_grid, text_1, font, 6, 3, 1, 2)

        text_1 = "ВТОРНИК"
        self.add_cell(main_grid, text_1, font, 7, 0, 1, 5)
        text_1 = "1\n9:00-\n10:35"
        self.add_cell(main_grid, text_1, font, 8, 0)
        text_1 = "\n\n\n"
        self.add_cell(main_grid, text_1, font, 8, 1, 1, 2)
        text_1 = "Языки и методы программирования\nЛагутина К.В\nауд. 216/221"
        self.add_cell(main_grid, text_1, font, 8, 3, 1, 2)
        text_1 = "2\n10:45-\n12:20"
        self.add_cell(main_grid, text_1, font, 9, 0)
        text_1 = "Теория вероятностей\nи\nматематическая статистика\nБогомолов Ю.В.\nауд.219"
        self.add_cell(main_grid, text_1, font, 9, 1, 1, 4)
        text_1 = "3\n13:20-\n14:55"
        self.add_cell(main_grid, text_1, font, 10, 0)
        text_1 = "Языки и методы программирования\nЛагутина К.В\nауд. 220"
        self.add_cell(main_grid, text_1, font, 10, 1, 1, 4)
        text_1 = "4\n15:05-\n16:40"
        self.add_cell(main_grid, text_1, font, 11, 0)
        text_1 = "ИЯзыки и методы программирования\nЛагутина К.В\nауд. 210"
        self.add_cell(main_grid, text_1, font, 11, 1, 1, 2)
        text_1 = "\n\n\n"
        self.add_cell(main_grid, text_1, font, 11, 3, 1, 2)
        text_1 = "5\n16:50-\n18:25"
        self.add_cell(main_grid, text_1, font, 12, 0)
        text_1 = "\n\n\n"
        self.add_cell(main_grid, text_1, font, 12, 1, 1, 2)
        text_1 = "\n\n\n"
        self.add_cell(main_grid, text_1, font, 12, 3, 1, 2)

        self.setLayout(main_grid)

    def add_cell(self, grid, text, font, row, col, row_span=1, col_span=1):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        frame.setStyleSheet("padding: 0px; margin: 0px, border-size: 0px")
        frame.setLineWidth(1)

        layout = QVBoxLayout()
        label = QLabel(text)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        frame.setLayout(layout)

        grid.addWidget(frame, row, col, row_span, col_span)

    def add_vertical_split_cell(self, grid, text1, text2, font, row, col, row_span=1, col_span=1):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        frame.setStyleSheet("padding: 0px; margin: 0px, border-size: 0px")
        frame.setLineWidth(1)

        split_layout = QGridLayout()
        split_layout.setSpacing(0)
        self.add_cell(split_layout, text1, font, 0, 0)
        self.add_cell(split_layout, text2, font, 1, 0)
        frame.setLayout(split_layout)

        grid.addWidget(frame, row, col, row_span, col_span)

    def add_horizontal_split_cell(self, grid, text1, text2, font, row, col, row_span=1, col_span=1):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        frame.setStyleSheet("padding: 0px; margin: 0px, border-size: 0px")
        frame.setLineWidth(1)

        split_layout = QGridLayout()
        split_layout.setSpacing(0)
        self.add_cell(split_layout, text1, font, 0,  0)
        self.add_cell(split_layout, text2, font, 0, 1)
        frame.setLayout(split_layout)

        grid.addWidget(frame, row, col, row_span, col_span)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Task1Window()
    window.show()
    sys.exit(app.exec())
