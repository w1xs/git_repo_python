import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QTextEdit, QLineEdit, QFormLayout, QBoxLayout, QListView, QFrame, QMessageBox,
                               QDialog, QCheckBox, QGridLayout)
from PySide6.QtCore import Qt, QPoint, QAbstractListModel, QModelIndex
from PySide6.QtGui import QDrag, QPixmap


class CheckboxDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModal(False)

        dialog_layout = QVBoxLayout()
        self.checkbox = QCheckBox("Соглашаюсь: ")
        self.checkbox.setStyleSheet("font-size: 20px")

        self.confirm_button = QPushButton("ОК")
        self.confirm_button.setStyleSheet("font-size: 20px")
        self.confirm_button.pressed.connect(self.accept)

        dialog_layout.addWidget(self.checkbox, alignment=Qt.AlignmentFlag.AlignCenter)
        dialog_layout.addWidget(self.confirm_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(dialog_layout)

    def get_checkbox_state(self) -> bool:
        return self.checkbox.isChecked()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 500, 500)
        main_layout = QGridLayout()

        self.open_dialog_button = QPushButton("Нажми")
        self.open_dialog_button.setStyleSheet("font-size: 20px")
        self.open_dialog_button.pressed.connect(self.open_dialog)

        self.label = QLabel("")
        self.label.setStyleSheet("font-size: 20px")

        main_layout.addWidget(self.open_dialog_button, 0, 0, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.label, 1, 0, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)

    def open_dialog(self):
        dialog = CheckboxDialog(self)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            if dialog.get_checkbox_state():
                self.label.setText("Checkbox выбран")
            else:
                self.label.setText("Checkbox не выбран")
        else:
            self.label.setText("Диалог закрыт без подтверждения")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
