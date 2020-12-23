import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Window.AuthWindow import AuthWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = AuthWindow()
    application.show()
    sys.exit(app.exec())