import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QSplineSeries
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики синуса и косинуса")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        chart = QChart()
        chart.setTitle("Графики функций")

        series_sin = QSplineSeries()
        series_sin.setName("sin(x)")

        series_cos = QSplineSeries()
        series_cos.setName("cos(x)")

        point_count = 300
        for i in range(++point_count):
            x = i * 2 * math.pi / point_count
            series_sin.append(x, math.sin(x))
            series_cos.append(x, math.cos(x))

        pen = QPen()
        pen.setWidth(4)
        pen.setColor("red")
        series_sin.setPen(pen)
        pen.setColor("green")
        series_cos.setPen(pen)
        chart.addSeries(series_sin)
        chart.addSeries(series_cos)

        chart.createDefaultAxes()

        chart_view = QChartView(chart)
        layout.addWidget(chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())