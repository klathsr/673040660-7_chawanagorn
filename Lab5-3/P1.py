
import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QSpinBox, QPushButton, QTableWidget,
    QTableWidgetItem, QHeaderView, QFrame
)
from PySide6.QtCore import Qt , QLocale
from PySide6.QtGui import QFont, QColor


def load_students(filepath="students.txt"):
    students = {}
    if not os.path.exists(filepath):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, "students.txt")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and "," in line:
                    student_id, name = line.split(",", 1)
                    students[student_id.strip()] = name.strip()
    except FileNotFoundError:
        print(f"Warning: students.txt not found at {filepath}")
    return students
  

def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


GRADE_COLORS = {
    "A": "#90EE90",
    "B": "#ADD8E6",
    "C": "#FFD700",
    "D": "#FFA07A",
    "F": "#FF6B6B",
}

QSS = """
QMainWindow, QWidget#centralWidget {
    background-color: #f0f0f0;
}
QLabel {
    font-size: 13px;
    color: #000000;
}
QComboBox {
    background-color: #ffffff;
    border: 1px solid #999999;
    border-radius: 2px;
    padding: 3px 6px;
    font-size: 13px;
    min-width: 155px;
    color: #000000;
}
QComboBox:focus { border: 1px solid #0078d7; }
QComboBox::drop-down { border: none; width: 18px; }
QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid #999999;
    selection-background-color: #0078d7;
    selection-color: #ffffff;
    color: #000000; 
}
QSpinBox {
    background-color: #ffffff;
    border: 1px solid #999999;
    border-radius: 2px;
    padding: 3px 4px;
    font-size: 13px;
    min-width: 65px;
    color: #000000;
}
QSpinBox:focus { border: 1px solid #0078d7; }

QPushButton#addBtn {
    background-color: #4a7fcb;
    color: #ffffff;
    border: none;
    border-radius: 3px;
    padding: 6px 20px;
    font-size: 13px;
    font-weight: bold;
}
QPushButton#addBtn:hover { background-color: #3567b3; }
QPushButton#addBtn:pressed { background-color: #2a519a; }

QPushButton#resetBtn {
    background-color: #eeeeee;
    color: #333333;
    border: 1px solid #aaaaaa;
    border-radius: 3px;
    padding: 6px 20px;
    font-size: 13px;
}
QPushButton#resetBtn:hover { background-color: #dddddd; }

QPushButton#clearBtn {
    background-color: #d9534f;
    color: #ffffff;
    border: none;
    border-radius: 3px;
    padding: 6px 20px;
    font-size: 13px;
    font-weight: bold;
}
QPushButton#clearBtn:hover { background-color: #c9302c; }

QFrame#inputArea {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    border-radius: 4px;
}

QTableWidget {
    background-color: #ffffff;
    gridline-color: #cccccc;
    border: 1px solid #cccccc;
    font-size: 13px;
    color: #000000;
}
QTableWidget::item { padding: 4px 8px; }
QTableWidget::item:selected {
    background-color: #cce4ff;
    color: #000000;
}
QHeaderView::section {
    background-color: #dce6f1;
    color: #000000;
    font-weight: bold;
    font-size: 13px;
    border: 1px solid #bbbbbb;
    padding: 5px 8px;
}
"""


class StudentGradeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.students = load_students()
        self.table_data = {}
        self.setWindowTitle("P1: Student scores and grades")
        self.setMinimumSize(860, 540)
        self.setup_ui()
        self.setStyleSheet(QSS)

    def setup_ui(self):
        central = QWidget()
        central.setObjectName("centralWidget")
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(12, 10, 12, 10)

        # ── Input Area ──────────────────────────────────
        input_area = QFrame()
        input_area.setObjectName("inputArea")
        input_layout = QVBoxLayout(input_area)
        input_layout.setSpacing(8)
        input_layout.setContentsMargins(14, 10, 14, 10)

        row1 = QHBoxLayout()
        row1.setSpacing(8)
        row1.addWidget(QLabel("Student ID:"))
        self.combo_student = QComboBox()
        self.combo_student.addItem("Select Student ID")
        for sid in sorted(self.students.keys()):
            self.combo_student.addItem(sid)
        self.combo_student.currentIndexChanged.connect(self.on_student_selected)
        row1.addWidget(self.combo_student)

        row1.addSpacing(24)
        row1.addWidget(QLabel("Student Name:"))
        self.name_label = QLabel("")
        self.name_label.setMinimumWidth(210)
        self.name_label.setStyleSheet(
            "border: 1px solid #999999; background: #ffffff; padding: 3px 8px; font-size: 13px;"
        )
        row1.addWidget(self.name_label)
        row1.addStretch()
        input_layout.addLayout(row1)

        row2 = QHBoxLayout()
        row2.setSpacing(8)
        row2.addWidget(QLabel("Math:"))
        self.spin_math = QSpinBox()
        self.spin_math.setRange(0, 100)
        row2.addWidget(self.spin_math)

        row2.addSpacing(16)
        row2.addWidget(QLabel("Science:"))
        self.spin_science = QSpinBox()
        self.spin_science.setRange(0, 100)
        row2.addWidget(self.spin_science)

        row2.addSpacing(16)
        row2.addWidget(QLabel("English:"))
        self.spin_english = QSpinBox()
        self.spin_english.setRange(0, 100)
        row2.addWidget(self.spin_english)

        row2.addStretch()
        input_layout.addLayout(row2)
        main_layout.addWidget(input_area)

        btn_row = QHBoxLayout()
        btn_row.setSpacing(8)

        self.btn_add = QPushButton("Add Student")
        self.btn_add.setObjectName("addBtn")
        self.btn_add.clicked.connect(self.add_student)

        self.btn_reset = QPushButton("Reset Input")
        self.btn_reset.setObjectName("resetBtn")
        self.btn_reset.clicked.connect(self.reset_input)

        self.btn_clear = QPushButton("Clear All")
        self.btn_clear.setObjectName("clearBtn")
        self.btn_clear.clicked.connect(self.clear_all)

        btn_row.addWidget(self.btn_add)
        btn_row.addWidget(self.btn_reset)
        btn_row.addWidget(self.btn_clear)
        btn_row.addStretch()
        main_layout.addLayout(btn_row)

        
        self.table = QTableWidget(0, 8)
        self.table.setHorizontalHeaderLabels([
            "Student ID", "Name", "Math", "Science", "English",
            "Total", "Average", "Grade"
        ])
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for col in [2, 3, 4, 5, 6, 7]:
            self.table.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeToContents)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().setVisible(True)
        main_layout.addWidget(self.table)

    def on_student_selected(self, index):
        if index <= 0:
            self.name_label.setText("")
        else:
            sid = self.combo_student.currentText()
            self.name_label.setText(self.students.get(sid, "Unknown"))

    def add_student(self):
        if self.combo_student.currentIndex() <= 0:
            return
        sid = self.combo_student.currentText()
        name = self.students.get(sid, "Unknown")
        math_s = self.spin_math.value()
        sci_s = self.spin_science.value()
        eng_s = self.spin_english.value()
        total = math_s + sci_s + eng_s
        average = total / 3
        grade = calculate_grade(average)
        self.table_data[sid] = {
            "name": name, "math": math_s, "science": sci_s,
            "english": eng_s, "total": total,
            "average": round(average, 2), "grade": grade,
        }
        self.refresh_table()

    def refresh_table(self):
        sorted_ids = sorted(self.table_data.keys())
        self.table.setRowCount(len(sorted_ids))
        for row, sid in enumerate(sorted_ids):
            d = self.table_data[sid]
            values = [
                sid, d["name"],
                str(d["math"]), str(d["science"]), str(d["english"]),
                str(d["total"]), f"{d['average']:.2f}", d["grade"]
            ]
            for col, val in enumerate(values):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignCenter)
                if col == 7:
                    item.setBackground(QColor(GRADE_COLORS.get(d["grade"], "#ffffff")))
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                elif col in (2, 3, 4) and int(val) < 50:
                    item.setBackground(QColor("#FFB3B3"))
                self.table.setItem(row, col, item)

    def reset_input(self):
        self.combo_student.setCurrentIndex(0)
        self.spin_math.setValue(0)
        self.spin_science.setValue(0)
        self.spin_english.setValue(0)
        self.name_label.setText("")

    def clear_all(self):
        self.table_data.clear()
        self.table.setRowCount(0)
        self.reset_input()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))
    app.setFont(QFont("Segoe UI", 10))
    window = StudentGradeCalculator()
    window.show()
    sys.exit(app.exec())
