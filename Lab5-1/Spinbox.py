import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Demo App")
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        spinbox = CustomSpinBox()
        layout.addWidget(spinbox, alignment=Qt.AlignCenter)

class CustomSpinBox(QSpinBox):
    def __init__(self):
        super().__init__()

        # Value range and step
        self.setRange(0, 100)
        self.setValue(50)
        self.setSingleStep(5)

        # Prefix and suffix
        self.setPrefix("$")
        self.setSuffix(" units")

        # Display format
        self.setDisplayIntegerBase(10)  # Decimal

        # Connect signals
        self.valueChanged.connect(self.on_value_changed)

    def on_value_changed(self, value):
        print(f"New value: {value}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()