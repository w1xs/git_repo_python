import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QPushButton, QListWidget, QListWidgetItem,
                               QLabel, QFileDialog, QMessageBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список картинок")
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Добавить картинку")
        self.add_button.clicked.connect(self.add_image)
        button_layout.addWidget(self.add_button)
        button_layout.addStretch()

        self.image_list = QListWidget()
        self.image_list.setIconSize(QSize(700, 500))
        self.image_list.setResizeMode(QListWidget.ResizeMode.Adjust)

        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.image_list)

        central_widget.setLayout(main_layout)

    def add_image(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите картинки",
            "",
            "Изображения (*.png *.jpg *.jpeg *.bmp *.gif *.tiff)"
        )

        if file_paths:
            for file_path in file_paths:
                pixmap = QPixmap(file_path)
                if not pixmap.isNull():
                    icon = QIcon(file_path)
                    item = QListWidgetItem(icon, os.path.basename(file_path))
                    item.setData(Qt.ItemDataRole.UserRole, file_path)
                    self.image_list.addItem(item)
                else:
                    QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить {file_path}")


def load_stylesheet(app, filename="style.qss"):
    try:
        with open(filename, 'r') as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print("Файл стилей не найден, используются стандартные стили")
    except Exception as e:
        print(f"Ошибка загрузки стилей: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_stylesheet(app, "task_2_style.qss")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())