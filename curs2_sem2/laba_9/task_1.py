import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QPen, QBrush, QLinearGradient, QColor, QPolygon


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Фигуры")
        self.setGeometry(100, 100, 600, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(Qt.GlobalColor.black, 2)
        painter.setPen(pen)

        triangle = QPolygon([
            QPoint(325, 30),
            QPoint(250, 110),
            QPoint(400, 110)
        ])
        painter.setBrush(QBrush(Qt.GlobalColor.yellow))
        painter.drawPolygon(triangle)

        painter.setBrush(QBrush(Qt.GlobalColor.red))
        painter.drawRect(250,160,150,150)

        gradient = QLinearGradient(50, 200, 150, 300)
        gradient.setColorAt(0.0, Qt.GlobalColor.blue)
        gradient.setColorAt(1.0, Qt.GlobalColor.red)
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(50, 200, 150, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())