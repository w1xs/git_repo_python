import sys
import csv
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget
from PySide6.QtCharts import QChart, QChartView, QScatterSeries, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анализ данных о деревьях")
        self.setGeometry(100, 100, 900, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        tabs = QTabWidget()

        data = self.load_data()

        scatter_tab = self.create_scatter_chart(data)
        tabs.addTab(scatter_tab, "Точечная диаграмма")

        bar_tab = self.create_bar_chart(data)
        tabs.addTab(bar_tab, "Столбчатая диаграмма")

        layout.addWidget(tabs)

    def load_data(self):
        data = []
        with open('../data_for_labs/trees.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    'id': int(row['ID']),
                    'girth': float(row['Girth']),
                    'height': float(row['Height']),
                    'volume': float(row['Volume'])
                })
        return data

    def create_scatter_chart(self, data):
        chart = QChart()
        chart.setTitle("Зависимость объема от диаметра")

        series = QScatterSeries()
        series.setName("Деревья")
        series.setMarkerSize(10)
        max_girth = 0
        max_volume = 0
        min_girth = 100
        min_volume = 100
        for tree in data:
            series.append(tree['girth'], tree['volume'])
            if tree['girth'] > max_girth:
                max_girth = tree['girth']
            if tree['girth'] < min_girth:
                min_girth = tree['girth']
            if tree['volume'] > max_volume:
                max_volume = tree['volume']
            if tree['volume'] < min_volume:
                min_volume = tree['volume']

        chart.addSeries(series)

        chart.createDefaultAxes()

        axis_x = chart.axes(Qt.Orientation.Horizontal)[0]
        axis_x.setTitleText("Диаметр (дюймы)")
        axis_x.setRange(min_girth-1,max_girth+1)

        axis_y = chart.axes(Qt.Orientation.Vertical)[0]
        axis_y.setTitleText("Объем (куб. футы)")
        axis_y.setRange(min_volume-3, max_volume+3)

        chart_view = QChartView(chart)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(chart_view)
        return widget

    def create_bar_chart(self, data):
        chart = QChart()
        chart.setTitle("Объем деревьев")

        series = QBarSeries()

        bar_set = QBarSet("Объем")
        categories = []

        for tree in data:
            bar_set.append(tree['volume'])
            categories.append(str(tree['id']))

        series.append(bar_set)
        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_x.setTitleText("ID дерева")
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText("Объем (куб. футы)")
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(chart_view)
        return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())