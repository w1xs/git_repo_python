import sys
from PIL.ImageQt import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,700,700)
        text_label_1 = QLabel("Нужно устроить перенос текста нa следующую строку", self)
        text_label_1.setGeometry(25,50,160,60)
        text_label_1.setWordWrap(True)
        text_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setItalic(True)
        font.setPointSize(8)
        text_label_1.setFont(font)

        text_label_2 = QLabel("But why?", self)
        text_label_2.move(25,100)
        text_label_2.setFixedSize(160,60)
        text_label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        font = QFont()
        font.setPointSize(16)
        text_label_2.setFont(font)

        text_label_1.setStyleSheet("margin: 5px;")
        text_label_2.setStyleSheet("margin: 5px;")

        picture_label = QLabel(self)
        picture = QPixmap("../data_for_labs/pinguin.png")
        if not picture.isNull():
            scaled_pixmap = picture.scaled(
                650, 600,
                Qt.AspectRatioMode.KeepAspectRatio,
            )
            picture_label.setPixmap(scaled_pixmap)
        else:
            print("Error with picture load")
        picture_label.move(215,25)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


