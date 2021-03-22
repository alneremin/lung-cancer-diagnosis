import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from Controller.controller import Controller

if __name__ == "__main__":
    app = QApplication([])
    application = Controller()
    sys.exit(app.exec())
