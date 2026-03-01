import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QCheckBox, QLineEdit, QFormLayout, QBoxLayout, QTabWidget, QFrame, QMessageBox)
from PySide6.QtCore import Qt, QPoint, QMimeData
from PySide6.QtGui import QDrag, QPixmap


class DraggableWidget(QLabel):

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            background-color: white;
            border: 2px solid black;
            padding: 5px;
        """)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(80, 40)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.text())
        drag.setMimeData(mime_data)

        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.position().toPoint())

        drag.exec()


class Task3Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Перетаскивание виджетов")
        self.setGeometry(200, 200, 600, 400)
        self.setAcceptDrops(True)
        self.separator = QFrame(self)
        self.separator.setStyleSheet("background-color: black;")
        self.widgets = []

    def resizeEvent(self, event):
        self.update_separator()

    def update_separator(self):
        mid_y = self.height() // 2
        self.separator.setGeometry(0, mid_y, self.width(), 2)

    def mousePressEvent(self, event):
        mid_y = self.height() // 2

        if event.position().y() < mid_y and event.button() == Qt.MouseButton.LeftButton:
            widget = DraggableWidget(f"Точка {len(self.widgets) + 1}", self)
            widget.move(int(event.position().x()) - 40, int(event.position().y()) - 20)
            widget.show()

            self.widgets.append(widget)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        drop_pos = event.position().toPoint()
        mid_y = self.height() // 2

        if drop_pos.y() >= mid_y:
            source_widget = event.source()
            if source_widget and source_widget in self.widgets:
                source_widget.move(drop_pos.x() - 40, drop_pos.y() - 20)
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        pos = event.position().toPoint()
        mid_y = self.height() // 2

        if pos.y() >= mid_y:
            event.accept()
        else:
            event.ignore()


