import sys
import os 
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QSpinBox,
    QPushButton, QMessageBox
)
from PySide6.QtCore import QLocale
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class SalesChartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monthly Sales Chart")
        self.resize(900, 600)

        self.sales_data = []

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        input_layout = QVBoxLayout()

    
        file_layout = QHBoxLayout()
        self.filename_input = QLineEdit()
        self.filename_input.setPlaceholderText("Enter filename (e.g., sales_data.txt)")
        file_layout.addWidget(QLabel("Filename:"))
        file_layout.addWidget(self.filename_input)
        input_layout.addLayout(file_layout)

        # Month
        self.month_combo = QComboBox()
        self.month_combo.addItems(
            ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        )

        # Sales Amount
        self.sales_input = QSpinBox()
        self.sales_input.setRange(0, 1000000)

        # Category
        self.category_combo = QComboBox()
        self.category_combo.addItems(
            ["Electronics", "Clothing", "Food", "Others"]
        )

        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("Month:"))
        form_layout.addWidget(self.month_combo)
        form_layout.addWidget(QLabel("Sales:"))
        form_layout.addWidget(self.sales_input)
        form_layout.addWidget(QLabel("Category:"))
        form_layout.addWidget(self.category_combo)

        input_layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()

        self.import_button = QPushButton("Import Data")
        self.add_button = QPushButton("Add Data")
        self.clear_button = QPushButton("Clear Chart")

        button_layout.addWidget(self.import_button)
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.clear_button)

        input_layout.addLayout(button_layout)

        main_layout.addLayout(input_layout)

        # ---------------- CHART SECTION ----------------
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # ---------------- SIGNALS ----------------
        self.import_button.clicked.connect(self.import_data)
        self.add_button.clicked.connect(self.add_data)
        self.clear_button.clicked.connect(self.clear_chart)

    # ---------------- FUNCTIONS ----------------

    def import_data(self):
        filename = self.filename_input.text()

        if not os.path.exists(filename):
            QMessageBox.warning(self, "Error", "File does not exist!")
            return

        try:
            with open(filename, "r") as file:
                self.sales_data.clear()
                for line in file:
                    month, sales, category = line.strip().split(",")
                    self.sales_data.append(
                        (month, int(sales), category)
                    )
            self.update_chart()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def add_data(self):
        month = self.month_combo.currentText()
        sales = self.sales_input.value()
        category = self.category_combo.currentText()

        self.sales_data.append((month, sales, category))
        self.update_chart()

    def clear_chart(self):
        self.sales_data.clear()
        self.figure.clear()
        self.canvas.draw()

    def update_chart(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        colors = {
            "Electronics": "blue",
            "Clothing": "green",
            "Food": "red",
            "Others": "orange"
        }

        for month, sales, category in self.sales_data:
            ax.bar(month, sales, color=colors.get(category, "gray"),
                   label=category)

        # ทำ legend ไม่ให้ซ้ำ
        handles, labels = ax.get_legend_handles_labels()
        unique = dict(zip(labels, handles))
        ax.legend(unique.values(), unique.keys())

        ax.set_title("Monthly Sales Chart")
        ax.set_xlabel("Months")
        ax.set_ylabel("Sales Amount")

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))
    window = SalesChartApp()
    window.show()
    sys.exit(app.exec())