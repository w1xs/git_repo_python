import sys
from PySide6.QtWidgets import QApplication

from Model import CaesarModel
from View import MainWindow
from Controller import CaesarController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = CaesarModel()
    view = MainWindow()
    controller = CaesarController(model, view)
    view.show()
    sys.exit(app.exec())