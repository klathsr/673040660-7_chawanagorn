import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget, QHBoxLayout,
                             QGridLayout, QFormLayout, QLineEdit,
                             QSpinBox, QPushButton)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont

class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        display_layout = QVBoxLayout()
        calc_type = QLabel("Standard")
        calc_type.setFont(QFont("Arial", 14, QFont.Bold))

        display = QLabel("899")
        display.setFont(QFont("Arial", 25))
        display.setAlignment(Qt.AlignRight)

        display_layout.addWidget(calc_type)
        display_layout.addWidget(display)

        layout = QGridLayout()

        self.setStyleSheet("""
            QPushButton {
                min-width: 60px;
                min-height: 40px;
                font-size: 16px;
            }
        """)

        # Basic grid positioning
        layout.addWidget(QPushButton("%"), 0, 0)  # row 0, col 0
        layout.addWidget(QPushButton("CE"), 0, 1)  # row 0, col 1
        layout.addWidget(QPushButton("C"), 0, 2)  # row 0, col 2
        layout.addWidget(QPushButton("<-"), 0, 3)
        
        layout.addWidget(QPushButton("1/x"), 1, 0)  # row 0, col 0
        layout.addWidget(QPushButton("x^2"), 1, 1)  # row 0, col 1
        layout.addWidget(QPushButton("sqrt(x)"), 1, 2)  # row 0, col 2
        layout.addWidget(QPushButton("/"), 1, 3)

        layout.addWidget(QPushButton("7"), 2, 0)  # row 0, col 0
        layout.addWidget(QPushButton("8"), 2, 1)  # row 0, col 1
        layout.addWidget(QPushButton("9"), 2, 2)  # row 0, col 2
        layout.addWidget(QPushButton("x"), 2, 3)

        layout.addWidget(QPushButton("4"), 3, 0)  # row 0, col 0
        layout.addWidget(QPushButton("5"), 3, 1)  # row 0, col 1
        layout.addWidget(QPushButton("6"), 3, 2)  # row 0, col 2
        layout.addWidget(QPushButton("-"), 3, 3)

        layout.addWidget(QPushButton("1"), 4, 0)  # row 0, col 0
        layout.addWidget(QPushButton("2"), 4, 1)  # row 0, col 1
        layout.addWidget(QPushButton("3"), 4, 2)  # row 0, col 2
        layout.addWidget(QPushButton("+"), 4, 3)

        layout.addWidget(QPushButton("+/-"), 5, 0)  # row 0, col 0
        layout.addWidget(QPushButton("0"), 5, 1)  # row 0, col 1
        layout.addWidget(QPushButton("."), 5, 2)  # row 0, col 2
        layout.addWidget(QPushButton("="), 5, 3)

        # Widget spanning multiple cells
        #layout.addWidget(QPushButton("0"), 3, 0, 1, 2)  # row 3, col 0, span 1 row, span 2 cols

        # Spacing and margins
        #layout.setSpacing(5)
        #layout.setContentsMargins(5, 5, 5, 5)

        # Column/Row stretch
        #layout.setColumnStretch(0, 1)  # First column stretches more
        #layout.setRowStretch(1, 2)     # Second row stretches more

        main_layout.addLayout(display_layout)
        main_layout.addLayout(layout)

        self.setLayout(main_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setCentralWidget(CalculatorLayout())
        self.resize(300, 500)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())