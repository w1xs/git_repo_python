import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
, QGroupBox, QPushButton, QTextEdit, QLineEdit, QFormLayout, QHeaderView, QListView, QTableView, QMessageBox)
from PySide6.QtCore import Qt, QPoint, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QDrag, QPixmap


class Product:

    def __init__(self, name, quantity, weight_per_unit):
        self.name = name
        self.quantity = int(quantity)
        self.weight_per_unit = float(weight_per_unit)

    def total_weight(self):
        return self.quantity * self.weight_per_unit


class ProductModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.headers = ["Название", "Количество", "Вес ед. (кг)", "Общий вес (кг)"]
        self.products = []

        self.products.append(Product("Молоко", 14, 1.0))
        self.products.append(Product("Говядина", 7, 0.25))
        self.products.append(Product("Бананы", 10, 0.1))

    def rowCount(self, parent=QModelIndex()):
        return len(self.products)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            product = self.products[index.row()]
            col = index.column()

            if col == 0:
                return product.name
            elif col == 1:
                return str(product.quantity)
            elif col == 2:
                return f"{product.weight_per_unit:.2f}"
            elif col == 3:
                return f"{product.total_weight():.2f}"

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.headers[section]
            else:
                return str(section + 1)
        return None

    def add_product(self, name, quantity, weight):
        self.beginInsertRows(QModelIndex(), len(self.products), len(self.products))
        self.products.append(Product(name, quantity, weight))
        self.endInsertRows()

    def total_weight_all(self):
        return sum(p.total_weight() for p in self.products)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список продуктов")
        self.setGeometry(200, 200, 700, 500)
        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()

        form_layout.addWidget(QLabel("Название:"))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Например: Виноград")
        form_layout.addWidget(self.name_input)

        form_layout.addWidget(QLabel("Кол-во:"))
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("5")
        form_layout.addWidget(self.quantity_input)

        form_layout.addWidget(QLabel("Вес ед. (кг):"))
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("0.2")
        form_layout.addWidget(self.weight_input)

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_product)
        form_layout.addWidget(self.add_button)

        self.model = ProductModel()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.total_label = QLabel()
        self.update_total_weight()

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.table_view)
        main_layout.addWidget(self.total_label)

        self.setLayout(main_layout)

    def add_product(self):
        name = self.name_input.text().strip()
        quantity = self.quantity_input.text().strip()
        weight = self.weight_input.text().strip()

        if not name or not quantity or not weight:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            quantity_val = int(quantity)
            weight_val = float(weight)

            if quantity_val <= 0 or weight_val <= 0:
                QMessageBox.warning(self, "Ошибка", "Количество и вес должны быть положительными")
                return

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Количество должно быть целым числом, вес - числом")
            return

        self.model.add_product(name, quantity_val, weight_val)

        self.name_input.clear()
        self.quantity_input.clear()
        self.weight_input.clear()

        self.update_total_weight()

    def update_total_weight(self):
        total = self.model.total_weight_all()
        self.total_label.setText(f"Общий вес всех продуктов: {total:.2f} кг")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
