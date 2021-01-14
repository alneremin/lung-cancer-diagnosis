from PyQt5 import QtWidgets, QtGui
from window.initauthorizationWindow import AuthorizationWindow
from window.initMainWindow import MainWindow

class Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(Controller, self).__init__()
        self.authorizationwindow = AuthorizationWindow()
        self.authorizationwindow.show()
        self.mainwindow = MainWindow()
        self.controll_clicked()

    def controll_clicked(self):
        self.authorizationwindow.window.button_entrance.clicked.connect(self.authorization)
        self.mainwindow.window.button_exit.clicked.connect(self.exit)

    def exit(self):
        self.mainwindow.close()
        self.authorizationwindow.show()
    
    def authorization(self):
        self.authorizationwindow.close()
        self.mainwindow.show()
