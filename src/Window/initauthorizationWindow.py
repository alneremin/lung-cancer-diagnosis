import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QPoint,QSize, pyqtSignal, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from Window.authorizationWindow import Ui_authorization

class Authorize(QObject):

    authorizeSignal = pyqtSignal()

class AuthorizationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AuthorizationWindow, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.window = Ui_authorization()
        self.window.setupUi(self)
        self.aut = Authorize()
        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setWindowFlag(Qt.WindowStaysOnTopHint)
        #self.window.tabBar.hide()
        #self.window.buttonClose.setText("{}".format('X'))
        #self.window.buttonInfo.setText("{}".format('?'))
        self.signalButtonClicked()

    def signalButtonClicked(self):
        pass
        #self.window.buttonClose.clicked.connect(self.closeWindow)

    def closeWindow(self):
        reply = QMessageBox.question(self,
                                     "Message",
                                     "Вы точно хотите закрыть приложение?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QtWidgets.QApplication.quit()
        else:
            pass
    
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
