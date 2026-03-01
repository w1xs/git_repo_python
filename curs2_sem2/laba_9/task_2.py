import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint, QParallelAnimationGroup, QSequentialAnimationGroup


class AnimatedWidget(QLabel):
    def __init__(self, color, size, parent=None):
        super().__init__(parent)
        self.setFixedSize(size, size)
        self.setStyleSheet(f"""
            background-color: {color};
            border: 2px solid black;
        """)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анимация фигур")
        self.setGeometry(100, 100, 600, 600)

        self.green_square = AnimatedWidget("green", 50, self)
        self.red_square = AnimatedWidget("red", 50, self)

        self.green_square.move(50, 50)
        self.red_square.move(50, 400)

        green_square_anim = QSequentialAnimationGroup()
        green_square_points = [
            QPoint(50, 50),
            QPoint(400, 50),
            QPoint(50, 400),
            QPoint(400, 400),
            QPoint(50, 50)
        ]

        for i in range(len(green_square_points) - 1):
            anim = QPropertyAnimation(self.green_square, b"pos")
            anim.setDuration(1500)
            anim.setStartValue(green_square_points[i])
            anim.setEndValue(green_square_points[i + 1])
            green_square_anim.addAnimation(anim)

        red_square_anim = QSequentialAnimationGroup()
        red_square_points = [
            QPoint(50, 400),
            QPoint(400, 400),
            QPoint(50, 50),
            QPoint(400, 50),
            QPoint(50, 400)
        ]
        for i in range(len(red_square_points) - 1):
            anim = QPropertyAnimation(self.red_square, b"pos")
            anim.setDuration(1500)
            anim.setStartValue(red_square_points[i])
            anim.setEndValue(red_square_points[i + 1])
            red_square_anim.addAnimation(anim)

        self.parallel_group = QParallelAnimationGroup()
        self.parallel_group.addAnimation(green_square_anim)
        self.parallel_group.addAnimation(red_square_anim)

        self.parallel_group.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
