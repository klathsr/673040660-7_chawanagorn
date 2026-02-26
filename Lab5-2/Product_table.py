## Complete Solution ##

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QSpinBox)
from PySide6.QtCore import Qt , QLocale
from PySide6.QtGui import QColor
import sys


class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Inventory Manager")
        self.setGeometry(100, 100, 600, 400)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Input section layout
        input_layout = QHBoxLayout()

        # Product Name input
        input_layout.addWidget(QLabel("Product Name:"))
        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Enter product name")
        input_layout.addWidget(self.product_input)

        # Quantity input
        input_layout.addWidget(QLabel("Quantity:"))
        self.quantity_input = QSpinBox()
        self.quantity_input.setMinimum(0)
        self.quantity_input.setMaximum(1000)
        self.quantity_input.setValue(0)
        input_layout.addWidget(self.quantity_input)

        # Add Product button
        add_btn = QPushButton("Add Product")
        add_btn.clicked.connect(self.add_product)
        input_layout.addWidget(add_btn)

        # Clear All button
        clear_btn = QPushButton("Clear Table")
        clear_btn.clicked.connect(self.clear_all)
        input_layout.addWidget(clear_btn)

        # add input layout to the main layout
        main_layout.addLayout(input_layout)

        # Table widget
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Product Name", "Quantity", "Status"])

        # set additional col properties
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 200)  # name col
        self.table.setColumnWidth(1, 100)  # quantity col

        # add table to the main layout
        main_layout.addWidget(self.table)

    def add_product(self):
        """Add a new product to the inventory table"""

        # get product data from the class object
        product_name = self.product_input.text().strip()
        quantity = self.quantity_input.value()

        # Validate input: product name
        if not product_name:
            return  # Don't add if name is empty

        # Determine status based on quantity
        if quantity < 10:
            status = "Low Stock"
            status_color = QColor(255, 200, 200)  # Light red
        else:
            status = "In Stock"
            status_color = QColor(200, 255, 200)  # Light green

        # Add new row to table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Add items to the row
        name_item = QTableWidgetItem(product_name)
        name_item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row_position, 0, name_item)

        quantity_item = QTableWidgetItem(str(quantity))
        quantity_item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row_position, 1, quantity_item)

        status_item = QTableWidgetItem(status)
        status_item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row_position, 2, status_item)

        # Color code the status
        status_item.setBackground(status_color)

        # Clear input fields
        self.product_input.clear()
        self.quantity_input.setValue(0)
        
        # Move the focus to the product input
        self.product_input.setFocus()

    def clear_all(self):
        """Clear all rows from the table"""
        self.table.setRowCount(0)


def main():
    app = QApplication(sys.argv)
    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates)) 
    window = InventoryApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()