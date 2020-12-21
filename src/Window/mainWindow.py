from PyQt5 import  QtCore, QtGui, QtWidgets
from ui.mainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    window: Ui_MainWindow

    def __init__(self):
        super(MainWindow, self).__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)