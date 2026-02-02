import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget, QLabel)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Demo App")
        self.setGeometry(100, 100, 500, 400)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # ComboBox - non-editable
        label1 = QLabel("Select Only (Not Editable):")
        non_editable_combo = NonEditableComboBox()

        # ComboBox - editable
        label2 = QLabel("Select or Type (Editable):")
        editable_combo = EditableComboBox()

        # Add to layout
        layout.addWidget(label1)
        layout.addWidget(non_editable_combo)
        layout.addWidget(label2)
        layout.addWidget(editable_combo)
        layout.addStretch()

class NonEditableComboBox(QComboBox):
    def __init__(self):
        super().__init__()

        # Add items
        self.addItems(sorted(["Pizza", "Pasta", "Sushi", "PadThai"]))

        # Non-editable (default is False, but this is for clarity)
        self.setEditable(False)

        # Set size
        self.setMinimumWidth(300)
        self.setMinimumHeight(40)

        # Connect signals
        self.currentIndexChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, index):
        print(f"Non-editable selected: {self.currentText()}")

class EditableComboBox(QComboBox):
    def __init__(self):
        super().__init__()

        # Add items
        self.addItems(sorted(["Pizza", "Pasta", "Sushi", "PadThai"]))

        # Make it editable
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.setCompleter(None)

        # Set size
        self.setMinimumWidth(300)
        self.setMinimumHeight(40)

        # Connect signals
        self.currentIndexChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, index):
        print(f"Editable selected/typed: {self.currentText()}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()