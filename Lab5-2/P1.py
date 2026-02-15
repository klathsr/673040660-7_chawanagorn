import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QComboBox, QVBoxLayout, QHBoxLayout, QGridLayout,
    QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(380, 600)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 20, 10, 20)
        main_layout.setSpacing(10)

        # ===== Title =====
        title = QLabel("Adult and Child BMI Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setFixedHeight(35)  
        title.setStyleSheet("""
        background-color:#b22222;
        color:White;
        font-weight:bold;
        font-size:14px;
        """)
        main_layout.addWidget(title)

        # ===== Age Group =====
        age_layout = QHBoxLayout()
        age_layout.addWidget(QLabel("BMI age group:"))

        self.age_combo = QComboBox()
        self.age_combo.addItems(["Adults 20+", "Children and Teenagers (5-19)"])
        age_layout.addWidget(self.age_combo)

        main_layout.addLayout(age_layout)

        # ===== Weight =====
        weight_layout = QHBoxLayout()
        weight_layout.addWidget(QLabel("Weight:"))

        self.weight_input = QLineEdit()
        weight_layout.addWidget(self.weight_input)

        self.weight_unit = QComboBox()
        self.weight_unit.addItems(["kilograms", "pounds"])
        weight_layout.addWidget(self.weight_unit)

        main_layout.addLayout(weight_layout)

        # ===== Height =====
        height_layout = QGridLayout()
        height_layout.addWidget(QLabel("Height:"), 0, 0)

        self.height_input1 = QLineEdit()
        height_layout.addWidget(self.height_input1, 0, 1)

        self.height_unit = QComboBox()
        self.height_unit.addItems(["centimeters", "meters", "feet"])
        height_layout.addWidget(self.height_unit, 0, 2)

        self.height_input2 = QLineEdit()
        self.height_input2_label = QLabel("inches")

        height_layout.addWidget(self.height_input2, 1, 1)
        height_layout.addWidget(self.height_input2_label, 1, 2)

        main_layout.addLayout(height_layout)

        # Hide inches unless feet selected
        self.height_unit.currentTextChanged.connect(self.toggle_height_fields)
        self.toggle_height_fields()

        # ===== Buttons =====
        btn_layout = QHBoxLayout()

        self.clear_btn = QPushButton("clear")
        self.submit_btn = QPushButton("Submit Registration")

        btn_layout.addWidget(self.clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.submit_btn)

        main_layout.addLayout(btn_layout)

        # ===== Result Container (Beige Background) =====
        self.result_container = QWidget()
        self.result_container.setStyleSheet("background-color: #FAF0E6;")

        self.result_layout = QVBoxLayout()
        self.result_layout.setAlignment(Qt.AlignCenter)

        self.result_title = QLabel("Your BMI")
        self.result_title.setAlignment(Qt.AlignCenter)
        self.result_title.setStyleSheet("""
            font-size:14px;
            font-weight:;
            color:Black;
        """)

        self.bmi_result = QLabel("0.00")
        self.bmi_result.setAlignment(Qt.AlignCenter)
        self.bmi_result.setStyleSheet("""
            font-size:40px;
            font-weight:bold;
            color:#3b5bdb;
        """)

        self.extra_info = QLabel("")
        self.extra_info.setAlignment(Qt.AlignCenter)
        self.extra_info.setWordWrap(True)
        self.extra_info.setOpenExternalLinks(True)

        self.result_layout.addWidget(self.result_title)
        self.result_layout.addWidget(self.bmi_result)
        self.result_layout.addWidget(self.extra_info)

        # ===== BMI Table (Adults Only) =====
        self.table = QTableWidget(4, 2)
        self.table.setHorizontalHeaderLabels(["BMI", "Condition"])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        bmi_data = [
            ("< 18.5", "Thin"),
            ("18.5 - 25.0", "Normal"),
            ("25.1 - 30.0", "Overweight"),
            ("> 30.0", "Obese")
        ]

        colors = ["#f9e79f", "#abebc6", "#f8c471", "#f1948a"]

        for row, (bmi, status) in enumerate(bmi_data):
            bmi_item = QTableWidgetItem(bmi)
            status_item = QTableWidgetItem(status)

            bmi_item.setBackground(QColor(colors[row]))
            status_item.setBackground(QColor(colors[row]))

            self.table.setItem(row, 0, bmi_item)
            self.table.setItem(row, 1, status_item)

        self.table.hide()  # hidden by default

        self.result_layout.addWidget(self.table)
        self.result_container.setLayout(self.result_layout)

        main_layout.addWidget(self.result_container)

        # ===== Connect Buttons =====
        self.submit_btn.clicked.connect(self.calculate_bmi)
        self.clear_btn.clicked.connect(self.clear_fields)

        self.setLayout(main_layout)

    # =========================
    # Toggle height fields
    # =========================
    def toggle_height_fields(self):
        if self.height_unit.currentText() == "feet":
            self.height_input2.show()
            self.height_input2_label.show()
        else:
            self.height_input2.hide()
            self.height_input2_label.hide()

    # =========================
    # Calculate BMI
    # =========================
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height_unit = self.height_unit.currentText()
            weight_unit = self.weight_unit.currentText()

            if weight <= 0:
                raise ValueError

            # Convert weight to kg
            if weight_unit == "pounds":
                weight *= 0.453592

            # Convert height to meters
            if height_unit == "centimeters":
                height = float(self.height_input1.text()) / 100
            elif height_unit == "meters":
                height = float(self.height_input1.text())
            elif height_unit == "feet":
                feet = float(self.height_input1.text())
                inches = float(self.height_input2.text() or 0)
                height = (feet * 12 + inches) * 0.0254

            if height <= 0:
                raise ValueError

            bmi = round(weight / (height ** 2), 2)
            self.bmi_result.setText(f"{bmi:.2f}")

            # ===== Adult Mode =====
            if self.age_combo.currentText() == "Adults 20+":
                self.table.show()
                self.extra_info.setText("")

            # ===== Child Mode =====
            else:
                self.table.hide()
                self.extra_info.setText(
                    'For child BMI interpretation, please click one of the following links:<br><br>'
                    '<a href="https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/">'
                    'BMI graph for BOYS</a><br>'
                    '<a href="https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/">'
                    'BMI graph for GIRLS</a>'
                )

        except ValueError:
            self.bmi_result.setText("0.00")
            self.extra_info.setText("")
            self.table.hide()

    # =========================
    # Clear Fields
    # =========================
    def clear_fields(self):
        self.weight_input.clear()
        self.height_input1.clear()
        self.height_input2.clear()
        self.bmi_result.setText("0.00")
        self.extra_info.setText("")
        self.table.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())
