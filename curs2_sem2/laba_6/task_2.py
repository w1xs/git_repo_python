import sys
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QTextEdit, QLineEdit, QFormLayout, QBoxLayout, QListView, QFrame,
                               QDialog, QCheckBox, QGridLayout, QMessageBox, QMenu)
from PySide6.QtCore import Qt, QPoint, QAbstractListModel, QModelIndex
from PySide6.QtGui import QDrag, QPixmap, QAction


class NoteModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.notes = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.notes)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= len(self.notes):
            return None

        note = self.notes[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            return f"{note['text'][:30]}... ({note['date']})"

        elif role == Qt.ItemDataRole.UserRole:
            return note['text']

        return None

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if not index.isValid() or index.row() >= len(self.notes):
            return False

        if role == Qt.ItemDataRole.EditRole:
            self.notes[index.row()]['text'] = value
            self.notes[index.row()]['date'] = datetime.now().strftime("%d.%m.%Y %H:%M (изменено)")
            self.dataChanged.emit(index, index)
            return True

        return False

    def add_note(self, text):
        self.beginInsertRows(QModelIndex(), len(self.notes), len(self.notes))
        self.notes.append({
            'text': text,
            'date': datetime.now().strftime("%d.%m.%Y %H:%M")
        })
        self.endInsertRows()

    def remove_note(self, row):
        if 0 <= row < len(self.notes):
            self.beginRemoveRows(QModelIndex(), row, row)
            del self.notes[row]
            self.endRemoveRows()
            return True
        return False


class NoteDialog(QDialog):
    def __init__(self, parent=None, note_text=""):
        super().__init__(parent)
        self.setWindowTitle("Заметка")
        self.setModal(True)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setText(note_text)
        self.text_edit.setStyleSheet("font-size: 20px;")

        button_layout = QHBoxLayout()
        self.save_btn = QPushButton("Сохранить")
        self.save_btn.setStyleSheet("font-size: 20px;")
        self.save_btn.clicked.connect(self.accept)

        self.cancel_btn = QPushButton("Отмена")
        self.cancel_btn.setStyleSheet("font-size: 20px;")
        self.cancel_btn.clicked.connect(self.reject)

        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.cancel_btn)

        layout.addWidget(QLabel("Текст заметки:"))
        layout.addWidget(self.text_edit)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_note_text(self):
        return self.text_edit.toPlainText().strip()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заметки")
        self.setGeometry(100, 100, 600, 500)
        self.model = NoteModel()
        main_layout = QVBoxLayout()
        title = QLabel("Мои заметки")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        add_button = QPushButton("Добавить заметку")
        add_button.setStyleSheet("font-size: 20px;")
        add_button.clicked.connect(self.add_note)
        self.list_view = QListView()
        self.list_view.setModel(self.model)
        self.list_view.setStyleSheet("font-size: 20px;")
        self.list_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_view.customContextMenuRequested.connect(self.show_context_menu)

        main_layout.addWidget(title)
        main_layout.addWidget(add_button)
        main_layout.addWidget(self.list_view)
        self.setLayout(main_layout)

    def add_note(self):
        dialog = NoteDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            text = dialog.get_note_text()
            if text:
                self.model.add_note(text)
            else:
                QMessageBox.warning(self, "Ошибка", "Текст заметки не может быть пустым")

    def edit_note(self, index):
        if not index.isValid():
            return

        current_text = self.model.data(index, Qt.ItemDataRole.UserRole)
        dialog = NoteDialog(self, current_text)
        dialog.setWindowTitle("Изменение заметки")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_text = dialog.get_note_text()
            if new_text:
                if self.model.setData(index, new_text, Qt.ItemDataRole.EditRole):
                    QMessageBox.information(self, "Успех", "Заметка изменена")
            else:
                QMessageBox.warning(self, "Ошибка", "Текст заметки не может быть пустым")

    def delete_note(self, index):
        if not index.isValid():
            return

        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Удалить заметку?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.model.remove_note(index.row())

    def show_context_menu(self, position):
        index = self.list_view.indexAt(position)
        if not index.isValid():
            return
        menu = QMenu()
        edit_action = QAction("Изменить", self)
        edit_action.triggered.connect(lambda: self.edit_note(index))
        delete_action = QAction("Удалить", self)
        delete_action.triggered.connect(lambda: self.delete_note(index))
        menu.addAction(edit_action)
        menu.addAction(delete_action)

        menu.exec(self.list_view.viewport().mapToGlobal(position))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())