from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QTextEdit, QPushButton, QMenuBar, QMenu,
                               QStatusBar, QFileDialog, QMessageBox, QDialog,
                               QFormLayout, QSpinBox, QComboBox, QDialogButtonBox,
                               QLabel)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QFont


class SettingsDialog(QDialog):
    def __init__(self, parent=None, step_size=3, side=0):
        super().__init__(parent)
        self.setWindowTitle("Настройки шифрования")

        layout = QFormLayout()

        self.step_size_spin = QSpinBox()
        self.step_size_spin.setRange(1, 100)
        self.step_size_spin.setValue(step_size)
        self.step_size_spin.setStyleSheet("font-size: 18px;")

        self.side_combo = QComboBox()
        self.side_combo.addItems(["Вправо", "Влево"])
        self.side_combo.setCurrentIndex(side)
        self.side_combo.setStyleSheet("font-size: 18px;")

        layout.addRow(QLabel("Сдвиг:"), self.step_size_spin)
        layout.addRow(QLabel("Направление:"), self.side_combo)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

        self.setLayout(layout)

    def get_settings(self):
        return self.step_size_spin.value(), self.side_combo.currentIndex()


class MainWindow(QMainWindow):
    encryptRequested = Signal(str)
    decryptRequested = Signal(str)
    settingsRequested = Signal()
    settingsChanged = Signal(int, int)
    openFileRequested = Signal()
    saveFileRequested = Signal()
    themeToggleRequested = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифр Цезаря")
        self.setGeometry(100, 100, 900, 600)

        font = QFont()
        font.setPointSize(22)
        self.setFont(font)

        self.setup_ui()
        self.setup_menu()
        self.statusBar().showMessage("Готов к работе")

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()

        text_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Исходный текст:"))
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Введите текст для шифрования...")
        left_layout.addWidget(self.input_text)

        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Зашифрованный текст:"))
        self.output_text = QTextEdit()
        self.output_text.setPlaceholderText("Введите текст для дефрования...")
        right_layout.addWidget(self.output_text)

        text_layout.addLayout(left_layout)
        text_layout.addLayout(right_layout)

        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.encrypt_btn = QPushButton("Зашифровать")
        self.encrypt_btn.setFixedSize(220, 50)
        self.encrypt_btn.clicked.connect(lambda: self.encryptRequested.emit(self.input_text.toPlainText()))

        self.decrypt_btn = QPushButton("Дешифровать")
        self.decrypt_btn.setFixedSize(220, 50)
        self.decrypt_btn.clicked.connect(lambda: self.decryptRequested.emit(self.output_text.toPlainText()))

        button_layout.addWidget(self.encrypt_btn)
        button_layout.addWidget(self.decrypt_btn)
        button_layout.addStretch()

        layout.addLayout(text_layout)
        layout.addLayout(button_layout)
        central.setLayout(layout)
        self.set_theme(False)

    def setup_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")

        open_action = QAction("Открыть", self)
        open_action.triggered.connect(self.openFileRequested.emit)
        file_menu.addAction(open_action)

        save_action = QAction("Сохранить", self)
        save_action.triggered.connect(self.saveFileRequested.emit)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        options_menu = menubar.addMenu("Опции")

        settings_action = QAction("Настройки шифрования", self)
        settings_action.triggered.connect(self.settingsRequested.emit)
        options_menu.addAction(settings_action)

        options_menu.addSeparator()

        theme_menu = options_menu.addMenu("Темы")

        light_action = QAction("Светлая тема", self)
        light_action.triggered.connect(self.themeToggleRequested.emit)
        theme_menu.addAction(light_action)

        dark_action = QAction("Темная тема", self)
        dark_action.triggered.connect(self.themeToggleRequested.emit)
        theme_menu.addAction(dark_action)

    def set_original_text(self, text):
        self.input_text.setText(text)

    def set_encrypted_text(self, text):
        self.output_text.setText(text)

    def set_status(self, message):
        self.statusBar().showMessage(message)

    def show_settings_dialog(self, step_size, side):
        dialog = SettingsDialog(self, step_size, side)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_step_size, new_side = dialog.get_settings()
            self.settingsChanged.emit(new_step_size, new_side)

    def show_error(self, message):
        QMessageBox.warning(self, "Ошибка", message)

    def show_open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовые файлы (*.txt)")
        return file_path

    def show_save_file_dialog(self, default_name):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", default_name, "Текстовые файлы (*.txt)")
        return file_path

    def set_theme(self, is_dark):
        if is_dark:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()

    def apply_light_theme(self):
        self.setStyleSheet("""
            QMainWindow, QDialog {
                background-color: #f5f5f5;
                color: #000000;
            }
            QTextEdit {
                background-color: white;
                color: black;
                border: 2px solid #cccccc;
                border-radius: 5px;
                padding: 8px;
                font-size: 22px;
            }
            QLabel {
                color: #333333;
                font-size: 22px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                font-size: 22px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QMenuBar {
                background-color: #e0e0e0;
                font-size: 18px;
            }
            QStatusBar {
                background-color: #e0e0e0;
                font-size: 16px;
            }
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow, QDialog {
                background-color: #2d2d2d;
                color: #ffffff;
            }
            QTextEdit {
                background-color: #3d3d3d;
                color: #ffffff;
                border: 2px solid #555555;
                border-radius: 5px;
                padding: 8px;
                font-size: 22px;
            }
            QLabel {
                color: #ffffff;
                font-size: 22px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #5a5a5a;
                color: white;
                border: 1px solid #777777;
                padding: 10px;
                font-size: 22px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #6a6a6a;
            }
            QMenuBar {
                background-color: #3d3d3d;
                color: white;
                font-size: 18px;
            }
            QStatusBar {
                background-color: #3d3d3d;
                color: white;
                font-size: 16px;
            }
        """)