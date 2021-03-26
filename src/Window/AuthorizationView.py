import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QPoint,QSize, pyqtSignal, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from Window.authorizationWindow import Ui_authorization

class Authorize(QObject):

    authorizeSignal = pyqtSignal()

class AuthorizationWindow(QtWidgets.QMainWindow):
    def __init__(self, model, controller):
        super(AuthorizationWindow, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.window = Ui_authorization()
        self.window.setupUi(self)
        self.model = model
        self.controller = controller
        self.controller.setView(self, 'AuthorizationWindow')

        self.initAll()
        

    aut = Authorize()

    def initAll(self):
        self.window.buttonEntrance.clicked.connect(self.authorize)
        self.aut.authorizeSignal.connect(self.authorize)
        self.show()

    def authorize(self):
        user = self.window.userName.text()
        password = self.window.userPassword.text()
        if self.model.authorize(user, password):
            self.controller.startWork(user)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Invalid user or password")
            #msg.setInformativeText('More information')
            msg.setWindowTitle("Attention!")
            msg.exec_()

    """
    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     "Message",
                                     "Вы точно хотите закрыть приложение?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.model.close()
            event.accept()
        else:
            event.ignore()
    """
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.aut.authorizeSignal.emit()
        event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = QPoint()

    def mouseMoveEvent(self, event):
        if not self.__press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.__press_pos))
