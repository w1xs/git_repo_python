from PySide6.QtCore import QObject


class CaesarController(QObject):
    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view

        self.view.encryptRequested.connect(self.handle_encrypt)
        self.view.decryptRequested.connect(self.handle_decrypt)
        self.view.settingsRequested.connect(self.handle_settings_request)
        self.view.settingsChanged.connect(self.handle_settings_change)
        self.view.openFileRequested.connect(self.handle_open_file)
        self.view.saveFileRequested.connect(self.handle_save_file)
        self.view.themeToggleRequested.connect(self.handle_theme_toggle)
        self.model.dataChanged.connect(lambda orig, enc: self.view.set_encrypted_text(enc))
        self.model.dataChanged.connect(lambda orig, enc: self.view.set_original_text(orig))

    def handle_encrypt(self, text):
        if text:
            self.model.encrypt(text)
            self.view.set_status("Текст зашифрован")
        else:
            self.view.show_error("Введите текст для шифрования")

    def handle_decrypt(self, text):
        if text:
            self.model.decrypt(text)
            self.view.set_status("Текст расшифрован")
        else:
            self.view.show_error("Введите текст для дешифрования")

    def handle_settings_request(self):
        step_size, side = self.model.get_settings()
        self.view.show_settings_dialog(step_size, side)

    def handle_settings_change(self, step_size, side):
        self.model.set_settings(step_size, side)
        self.view.set_status(
            f"Настройки изменены: сдвиг={step_size}, направление={'вправо' if side == 0 else 'влево'}")

    def handle_open_file(self):
        file_path = self.view.show_open_file_dialog()
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.view.set_original_text(content)
                self.view.set_status(f"Файл загружен: {file_path.split('/')[-1]}")
            except Exception as e:
                self.view.show_error(f"Не удалось прочитать файл: {e}")

    def handle_save_file(self):
        text = self.model.encrypted_text
        if not text:
            self.view.show_error("Нет данных для сохранения")
            return

        file_path = self.view.show_save_file_dialog("encrypted.txt")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                self.view.set_status(f"Файл сохранен: {file_path.split('/')[-1]}")
            except Exception as e:
                self.view.show_error(f"Не удалось сохранить файл: {e}")

    def handle_theme_toggle(self):
        is_dark = self.model.toggle_theme()
        self.view.set_theme(is_dark)
        theme_name = "темная" if is_dark else "светлая"
        self.view.set_status(f"{theme_name.capitalize()} тема активирована")