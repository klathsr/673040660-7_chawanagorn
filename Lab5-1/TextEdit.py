import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCharFormat, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Demo App")
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        check_box = CustomTextEdit()
        layout.addWidget(check_box, alignment=Qt.AlignCenter)

class CustomTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()

        # Basic setup
        self.setPlaceholderText("Enter your text here...")
        self.setAcceptRichText(True)

        # Text formatting
        self.setFontFamily("Arial")
        self.setFontPointSize(12)

        # Document settings
        self.document().setMaximumBlockCount(100)  # Line limit

        # Connect signals
        self.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        text_content = self.toPlainText() # toHtml()
        print("text:", text_content)

    def highlight_text(self, color):
        format = QTextCharFormat()
        format.setBackground(QColor(color))
        self.textCursor().mergeCharFormat(format)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()