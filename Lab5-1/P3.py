import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QComboBox, QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(380, 600)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # ===== Title =====
        title = QLabel("Adult and Child BMI Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            background-color:#c0503c;
            color:white;
            font-weight:bold;
            padding:8px;
            border-radius:4px;
        """)
        main_layout.addWidget(title)

        # ===== Age Type =====
        age_layout = QHBoxLayout()
        age_layout.addWidget(QLabel("Calculate BMI for"))

        self.age_combo = QComboBox()
        self.age_combo.addItems(["Adult Age 20+", "Child Age 2-19"])
        age_layout.addWidget(self.age_combo)

        main_layout.addLayout(age_layout)

        # ===== Weight =====
        weight_layout = QHBoxLayout()
        weight_layout.addWidget(QLabel("Weight:"))

        self.weight_input = QLineEdit()
        self.weight_input.setFixedWidth(80)
        weight_layout.addWidget(self.weight_input)

        self.weight_unit = QComboBox()
        self.weight_unit.addItems(["pounds", "kilograms"])
        weight_layout.addWidget(self.weight_unit)

        main_layout.addLayout(weight_layout)

        # ===== Height =====
        height_layout = QGridLayout()
        height_layout.addWidget(QLabel("Height:"), 0, 0)

        self.height_input1 = QLineEdit()
        self.height_input1.setFixedWidth(70)
        height_layout.addWidget(self.height_input1, 0, 1)

        self.height_unit = QComboBox()
        self.height_unit.addItems(["centimeters", "meters", "feet"])
        height_layout.addWidget(self.height_unit, 0, 2)

        self.height_input2 = QLineEdit()
        self.height_input2.setFixedWidth(70)
        height_layout.addWidget(self.height_input2, 1, 1)

        self.height_input2_label = QLabel("inches")
        height_layout.addWidget(self.height_input2_label, 1, 2)

        main_layout.addLayout(height_layout)

        # ===== Buttons =====
        btn_layout = QHBoxLayout()

        self.clear_btn = QPushButton("Clear")
        self.calculate_btn = QPushButton("Calculate")

        btn_layout.addWidget(self.clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.calculate_btn)

        main_layout.addLayout(btn_layout)

        # ===== Answer Section =====
        answer_frame = QFrame()
        answer_frame.setFrameShape(QFrame.StyledPanel)
        answer_layout = QVBoxLayout()

        answer_layout.addWidget(QLabel("Answer:"))

        self.bmi_result = QLabel("BMI = ")
        self.bmi_result.setAlignment(Qt.AlignCenter)
        self.bmi_result.setStyleSheet("font-weight:bold; font-size:14px;")

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)

        answer_layout.addWidget(self.bmi_result)
        answer_layout.addWidget(self.status_label)

        # ===== BMI Table =====
        table_label = QLabel("Adult BMI")
        table_label.setAlignment(Qt.AlignCenter)
        table_label.setStyleSheet("font-weight:bold;")
        answer_layout.addWidget(table_label)

        self.table = QTableWidget(4, 2)
        self.table.setHorizontalHeaderLabels(["BMI", "Status"])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        bmi_data = [
            ("< 18.5", "Underweight"),
            ("18.5 - 24.9", "Healthy Weight"),
            ("25.0 - 29.9", "Overweight"),
            ("≥ 30.0", "Obese")
        ]

        colors = ["#f9e79f", "#abebc6", "#f8c471", "#f1948a"]

        for row, (bmi, status) in enumerate(bmi_data):
            bmi_item = QTableWidgetItem(bmi)
            status_item = QTableWidgetItem(status)

            bmi_item.setBackground(QColor(colors[row]))
            status_item.setBackground(QColor(colors[row]))

            self.table.setItem(row, 0, bmi_item)
            self.table.setItem(row, 1, status_item)

        answer_layout.addWidget(self.table)
        answer_frame.setLayout(answer_layout)
        main_layout.addWidget(answer_frame)

        # ===== Connect Buttons =====
        self.calculate_btn.clicked.connect(self.calculate_bmi)
        self.clear_btn.clicked.connect(self.clear_fields)

        self.setLayout(main_layout)

    # =========================
    # Calculate BMI Function
    # =========================
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height_unit = self.height_unit.currentText()
            weight_unit = self.weight_unit.currentText()

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
                total_inches = feet * 12 + inches
                height = total_inches * 0.0254

            bmi = weight / (height ** 2)
            bmi = round(bmi, 1)

            self.bmi_result.setText(f"BMI = {bmi}")

            if bmi < 18.5:
                status = "Underweight"
            elif bmi < 25:
                status = "Healthy Weight"
            elif bmi < 30:
                status = "Overweight"
            else:
                status = "Obese"

            self.status_label.setText(status)

        except:
            self.bmi_result.setText("Invalid Input")
            self.status_label.setText("")

    # =========================
    # Clear Function
    # =========================
    def clear_fields(self):
        self.weight_input.clear()
        self.height_input1.clear()
        self.height_input2.clear()
        self.bmi_result.setText("BMI = ")
        self.status_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())