import sys
import csv
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анализ ураганов")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        tabs = QTabWidget()

        data = self.load_data()

        tabs.addTab(self.create_2007_chart(data), "Ураганы 2007 по месяцам")
        tabs.addTab(self.create_yearly_chart(data), "Ураганы по годам")

        layout.addWidget(tabs)

    def load_data(self):
        data = []
        with open('../data_for_labs/hurricanes.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    'month': row['Month'],
                    '2007': int(row['2007']),
                    '2005': int(row['2005']),
                    '2006': int(row['2006']),
                    '2008': int(row['2008']),
                    '2009': int(row['2009']),
                    '2010': int(row['2010']),
                    '2011': int(row['2011']),
                    '2012': int(row['2012']),
                    '2013': int(row['2013']),
                    '2014': int(row['2014']),
                    '2015': int(row['2015'])
                })
        return data

    def create_2007_chart(self, data):
        series = QPieSeries()

        max_value = 0
        max_month = ""

        for row in data:
            value = row['2007']
            if value > 0:
                series.append(row['month'], value)
                if value > max_value:
                    max_value = value
                    max_month = row['month']

        for slice in series.slices():
            if slice.label() == max_month:
                slice.setExploded(True)
                slice.setLabelVisible(True)
                slice.setColor(QColor("red"))

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Ураганы 2007 года по месяцам")

        chart_view = QChartView(chart)
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(chart_view)
        return widget

    def create_yearly_chart(self, data):
        yearly_totals = {}

        years = []
        for key in data[0].keys():
            print(key)
            years.append(key)
        years = years[1:]
        years = sorted(years)

        for year in years:
            yearly_totals[year] = 0

        for row in data:
            for year in years:
                yearly_totals[year] += row[year]

        series = QPieSeries()

        min_value = float('inf')
        min_year = ""

        for year, total in yearly_totals.items():
            if total > 0:
                series.append(year, total)
                if total < min_value:
                    min_value = total
                    min_year = year

        for slice in series.slices():
            if slice.label() == min_year:
                slice.setExploded(True)
                slice.setLabelVisible(True)
                slice.setColor(QColor("red"))

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Ураганы по годам")

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