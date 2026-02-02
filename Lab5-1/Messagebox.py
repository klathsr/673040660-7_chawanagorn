import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Demo App")
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)



# Note: this one doesn't inherit from QMessageBox
class CustomMessageBox:
    @staticmethod
    def show_info(title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)

        return msg.exec()

    @staticmethod
    def show_question(title, question):
        return QMessageBox.question(
            None,
            title,
            question,
            QMessageBox.Yes | QMessageBox.No
        )

    @staticmethod
    def show_warning(title, message):
        return QMessageBox.warning(
            None,
            title,
            message,
            QMessageBox.Ok
        )

def main():
    # Create Main App
    app = QApplication(sys.argv)


    CustomMessageBox.show_info("Hello","Hello Guys, How are you doing?")
    CustomMessageBox.show_question("Quit?","Do you want to give up?")
    CustomMessageBox.show_warning("Quit?","Give up will make your mom blow up!")

    #window = MainWindow()
    #window.show()
    #sys.exit(app.exec())

if __name__ == "__main__":
    main()