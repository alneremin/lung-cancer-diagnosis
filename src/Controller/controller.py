from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
from Window.initAuthorizationWindow import AuthorizationWindow
from Window.initMainWindow import MainWindow
from Database.database import Database

class Controller():
    def __init__(self):
        #super(Controller, self).__init__()
        self.authorizationWindow = AuthorizationWindow()
        self.authorizationWindow.show()
        self.mainWindow = MainWindow()
        self.settings = QSettings('settings.conf', QSettings.IniFormat)
        self.db = Database(self.settings.value('driver'), self.settings.value('db_path'))
        self.db.createConnection()

        self.fillTable()
        self.controllClicked()

    def controllClicked(self):
        self.authorizationWindow.window.button_entrance.clicked.connect(self.authorization)
        self.authorizationWindow.aut.authorizeSignal.connect(self.authorization)

        self.mainWindow.window.button_exit.clicked.connect(self.exit)

    def exit(self):
        self.mainWindow.close()
        self.authorizationWindow.show()
    
    def authorization(self):
        user = self.authorizationWindow.window.user_name.text()
        password = self.authorizationWindow.window.user_password.text()
        if self.db.authorize(user, password):
            self.authorizationWindow.close()
            self.mainWindow.window.User.setText(user)
            self.mainWindow.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Invalid user or password")
            #msg.setInformativeText('More information')
            msg.setWindowTitle("Attention!")
            msg.exec_()

    def search(self):
        pass

    def fillTable(self):
        data = self.db.getPatients()
        self.mainWindow.window.tablePatient.clear()
        for row in data:
            rows = self.mainWindow.window.tablePatient.rowCount()
            self.mainWindow.window.tablePatient.setRowCount(rows + 1)
            for j in range(len(row)):
                self.mainWindow.window.tablePatient.setItem(rows, j, QTableWidgetItem(row[j]))
            #self.mainWindow.window.tablePatient.insertRow(self.mainWindow.window.tablePatient.rowCount())
            #model = self.mainWindow.window.tablePatient.selectionModel()
            #model.insertRow(0)#.addItem(" ".join(row[1:4]))
