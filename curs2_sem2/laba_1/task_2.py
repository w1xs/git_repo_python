import Book
import sys
from PIL.ImageQt import QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 700)
        books = [
            Book.Book("Ведьмак: Час Презрения",
                      "Анджей Сапковский",
                      336,
                      "../data_for_labs/The Witcher.png"
                      ),
            Book.Book("Хоббит",
                      "Джон Рональд Роуэл Толкиен",
                      288,
                      "../data_for_labs/Hobbit.png"
                      ),
            Book.Book("Водители фрегатов",
                      "Николай Корнеевич Чуковский",
                      320,
                      "../data_for_labs/Fregat.png"
                      )
        ]
        main_layout = QVBoxLayout()
        for book in books:
            book_group = QGroupBox()
            group_layout = QHBoxLayout()
            picture_label = QLabel()
            picture_label.setFixedSize(200,250)
            picture = QPixmap(book.cover_url)
            if not picture.isNull():
                scaled_pixmap = picture.scaled(
                    200, 250,
                    Qt.AspectRatioMode.KeepAspectRatio,
                )
                picture_label.setPixmap(scaled_pixmap)
            else:
                print(f"Error with {book.name} picture load")

            text_label = QLabel(book.get_info())
            font = QFont()
            font.setPointSize(16)
            text_label.setFont(font)

            group_layout.addWidget(picture_label)
            group_layout.addWidget(text_label)

            book_group.setLayout(group_layout)
            main_layout.addWidget(book_group)

        main_layout.addStretch()
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())