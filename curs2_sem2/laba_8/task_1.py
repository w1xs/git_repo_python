import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout,
                               QGroupBox, QPushButton, QTextEdit, QLineEdit, QFormLayout,
                               QListView, QFrame, QMessageBox)
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex

# """
# Код взят из laba_5 task_1
# """

class NoteBookModel(QAbstractListModel):
    def __init__(self, note_list: list):
        super().__init__()
        self.note_list = note_list

    def rowCount(self, parent=None):
        return len(self.note_list)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self.note_list[index.row()]
        return None

    def add_note(self, text: str):
        self.beginInsertRows(QModelIndex(), len(self.note_list), len(self.note_list))
        self.note_list.append(text)
        self.endInsertRows()

    def delete_note(self, row: int):
        if 0 <= row < len(self.note_list):
            self.beginRemoveRows(QModelIndex(), row, row)
            del self.note_list[row]
            self.endRemoveRows()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 700, 700)

        self.model = NoteBookModel([])

        main_layout = QHBoxLayout()

        right_box = QFrame()
        right_layout = QVBoxLayout()
        right_box.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        right_box.setLineWidth(1)

        right_header = QLabel("Добавить заметку")
        right_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_note_field = QTextEdit()
        self.add_note_field.setPlaceholderText("Введите текст заметки")
        self.add_note_field.setMinimumSize(300, 500)
        self.add_note_field.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.add_note_field.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        self.add_note_button = QPushButton("Добавить")
        self.add_note_button.setMinimumSize(100, 50)
        self.add_note_button.clicked.connect(self.add_note)

        right_layout.addWidget(right_header)
        right_layout.addWidget(self.add_note_field)
        right_layout.addWidget(self.add_note_button)
        right_box.setLayout(right_layout)

        left_box = QFrame()
        left_layout = QVBoxLayout()
        left_box.setFrameStyle(QFrame.Shape.Box)
        left_box.setLineWidth(0)

        left_header = QLabel("Список заметок")
        left_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.note_list = QListView()
        self.note_list.setModel(self.model)

        self.note_list.clicked.connect(self.on_note_clicked)

        left_layout.addWidget(left_header)
        left_layout.addWidget(self.note_list)
        left_box.setLayout(left_layout)

        main_layout.addWidget(left_box, stretch=3)
        main_layout.addWidget(right_box, stretch=1)
        self.setLayout(main_layout)

    def on_note_clicked(self, index):
        row = index.row()
        note_text = self.model.note_list[row]
        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            f"Удалить заметку '{note_text}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.model.delete_note(row)

    def add_note(self):
        text = self.add_note_field.toPlainText().strip()
        if text:
            self.model.add_note(text)
            self.add_note_field.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите текст заметки")


def load_stylesheet(app, filename="style.qss"):
    try:
        with open(filename, 'r') as file:
            app.setStyleSheet(file.read())
        print(f"Стили загружены из {filename}")
    except FileNotFoundError:
        print(f"Файл стилей {filename} не найден")
    except Exception as e:
        print(f"Ошибка при загрузке стилей: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_stylesheet(app, "task_1_style.qss")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())