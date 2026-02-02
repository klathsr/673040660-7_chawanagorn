import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Demo App")
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # ----------------------------------------------------
        # Text label
        # ----------------------------------------------------
        # 1) Create Widget
        text_label = QLabel("Hello World")
        text_label.setFont(QFont("Arial", 14, QFont.Bold))
        text_label.setAlignment(Qt.AlignCenter)

        # 2) Add the widget to layout
        layout.addWidget(text_label)

        # ----------------------------------------------------
        # Image label
        # ----------------------------------------------------
        # 1) Create Widget
        image_label = QLabel()
        try:
            pixmap = QPixmap("qrcode.jpg")
            image_label.setPixmap(pixmap.scaled(
                200, 200,  # width, height
                Qt.KeepAspectRatio,  # maintain aspect ratio
                Qt.SmoothTransformation  # smooth scaling
            ))
        except:
            # Fallback if image not found
            image_label.setText("Image not found: image.png")
            image_label.setAlignment(Qt.AlignCenter)

        image_label.setAlignment(Qt.AlignCenter)

        # 2) Add the widget to layout
        layout.addWidget(image_label)

        # ----------------------------------------------------
        # Rich text label
        # ----------------------------------------------------
        # 1) Create Widget
        rich_label = QLabel()
        rich_label.setText("<h1>Title</h1><p>This is <b>bold</b> and <i>italic</i> text</p>")
        rich_label.setTextFormat(Qt.RichText)
        rich_label.setOpenExternalLinks(True)  # Allow clicking links
        rich_label.setAlignment(Qt.AlignCenter)

        # 2) Add the widget to layout
        layout.addWidget(rich_label)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()