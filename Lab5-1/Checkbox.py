import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QCheckBox, QPushButton, QGroupBox,
                               QMessageBox)
from PySide6.QtCore import Qt

class CheckboxOptionsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox Options Example")
        self.setMinimumSize(400, 250)

        # Main widget and layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # 1) Create options group (all checkboxes)
        self.create_food_preferences_group()

        # 2) Button to get selected options
        submit_button = QPushButton("Submit Choices")
        submit_button.clicked.connect(self.show_selected_options)

        # 3) Add widgets to main layout
        main_layout.addWidget(self.food_group)
        main_layout.addWidget(submit_button)
        main_layout.addStretch() # space spreading management

        self.setCentralWidget(central_widget)

    def create_food_preferences_group(self):
        self.food_group = QGroupBox("Food Preferences")
        layout = QVBoxLayout()

        # Create multiple checkboxes
        self.pizza_cb = QCheckBox("Pizza")
        self.burger_cb = QCheckBox("Burger")
        self.pasta_cb = QCheckBox("Pasta")
        self.salad_cb = QCheckBox("Salad")

        # Setting initial states (optional)
        self.pasta_cb.setChecked(True)

        # Adding checkboxes to layout of this group
        layout.addWidget(self.pizza_cb)
        layout.addWidget(self.burger_cb)
        layout.addWidget(self.pasta_cb)
        layout.addWidget(self.salad_cb)

        # set layout of this group
        self.food_group.setLayout(layout)

    def show_selected_options(self):
        food_options = []
        if self.pizza_cb.isChecked():
            food_options.append("Pizza")
        if self.burger_cb.isChecked():
            food_options.append("Burger")
        if self.pasta_cb.isChecked():
            food_options.append("Pasta")
        if self.salad_cb.isChecked():
            food_options.append("Salad")

        message = "Selected Food Options:\n"
        message += ", ".join(food_options) if food_options else "None"

        QMessageBox.information(self, "Selected Options", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckboxOptionsWindow()
    window.show()
    sys.exit(app.exec())