import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget)
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Demo App")
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 1) Create an instance of the button class
        button = CustomButton()

        # 2) Add button to layout
        layout.addWidget(button,alignment=Qt.AlignCenter)


class CustomButton(QPushButton):
    def __init__(self):
        super().__init__()

        # Basic setup
        self.setText("Click Me")
        self.setIcon(QIcon("icon.png"))
        self.setCheckable(True)  # Toggle button

        # Size configurations
        self.setFixedSize(120, 40)  # Fixed width and height
        self.setIconSize(QSize(20, 20))

        # Connect signals
        self.clicked.connect(self.handle_click)
        self.toggled.connect(self.handle_toggle)

    def handle_click(self):
        print("Button clicked!")

    def handle_toggle(self, checked):
        print(f"Button toggled: {checked}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()