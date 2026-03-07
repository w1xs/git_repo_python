from PySide6.QtCore import QObject, Signal
from Cesar import Cesar


class CaesarModel(QObject):
    dataChanged = Signal(str, str)
    settingsChanged = Signal(int, int)

    def __init__(self):
        super().__init__()
        self.original_text = ""
        self.encrypted_text = ""
        self.step_size = 3
        self.side = 0
        self.dark_theme = False

    def encrypt(self, text):
        self.original_text = text
        cesar = Cesar(text, self.side, self.step_size)
        self.encrypted_text = cesar.encrypt()
        self.dataChanged.emit(self.original_text, self.encrypted_text)
        return self.encrypted_text

    def decrypt(self, text):
        self.encrypted_text = text
        cesar = Cesar(text, self.side, self.step_size)
        self.original_text = cesar.decrypt()
        self.dataChanged.emit(self.original_text, self.encrypted_text)
        return self.original_text

    def set_settings(self, step_size, side):
        self.step_size = step_size
        self.side = side
        self.settingsChanged.emit(step_size, side)

    def get_settings(self):
        return self.step_size, self.side

    def get_theme(self):
        return self.dark_theme

    def toggle_theme(self):
        self.dark_theme = not self.dark_theme
        return self.dark_theme