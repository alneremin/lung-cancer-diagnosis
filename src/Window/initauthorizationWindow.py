import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QPoint,QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from window.authorizationWindow import Ui_authorization

class AuthorizationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AuthorizationWindow, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.window = Ui_authorization()
        self.window.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.window.button_close.setText("{}".format('X'))
        self.window.button_info.setText("{}".format('?'))
        self.signal_button_clicked()

    def signal_button_clicked(self):
        self.window.button_close.clicked.connect(self.close_window)

    def close_window(self):
        reply = QMessageBox.question(self,
                                     "Message",
                                     "Вы точно хотите закрыть приложение?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QtWidgets.QApplication.quit()
        else:
            pass
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = QPoint()

    def mouseMoveEvent(self, event):
        if not self.__press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.__press_pos))
