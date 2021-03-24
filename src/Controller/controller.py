from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSettings, QObject, pyqtSignal
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
from MIA.mia import MIA
import threading
from queue import Queue
import time
from io import BytesIO
from PIL import Image
import traceback
import logging

class Controller(QObject):
    def __init__(self):
        super(Controller, self).__init__()
        self.authorizationWindow = AuthorizationWindow()
        self.authorizationWindow.show()
        self.mainWindow = MainWindow()
        self.settings = QSettings('settings.conf', QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")
        self.db = Database(self.settings.value('driver'), self.settings.value('db_path'))
        self.db.createConnection()
        self.mia = MIA(self.settings.value('model_path'))
        #self.q = Queue()
        
        self.inProgress.connect(self.changeProgressBar)
        self.fillTable()
        self.controllClicked()

    inProgress = pyqtSignal(list)

    def controllClicked(self):
        self.authorizationWindow.window.buttonEntrance.clicked.connect(self.authorization)
        self.authorizationWindow.aut.authorizeSignal.connect(self.authorization)

        self.mainWindow.window.buttonExit.clicked.connect(self.exit)
        self.mainWindow.window.buttonAddPatientInDB.clicked.connect(self.addPatient)
        self.mainWindow.window.buttonAddPatientInDB.clicked.connect(lambda: self.mainWindow.window.tabWidget.setCurrentIndex(0))
        self.mainWindow.window.buttonStartAnalyze.clicked.connect(self.startAnalyze)
        self.mainWindow.window.saveDB.clicked.connect(self.saveResults)
    def exit(self):
        self.mainWindow.close()
        self.authorizationWindow.show()
    
    def authorization(self):
        user = self.authorizationWindow.window.userName.text()
        password = self.authorizationWindow.window.userPassword.text()
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

    def fillTable(self):
        data = self.db.getPatients()
        #currentRow = self.mainWindow.window.tablePatient.currentRow()
        self.mainWindow.window.tablePatient.setRowCount(0)
        for row in data:
            self.addRowInTable(row)
            #self.mainWindow.window.tablePatient.insertRow(self.mainWindow.window.tablePatient.rowCount())
            #model = self.mainWindow.window.tablePatient.selectionModel()
            #model.insertRow(0)#.addItem(" ".join(row[1:4]))
        #self.mainWindow.window.tablePatient.setCurrentCell(currentRow, 0)

    def addRowInTable(self, rowData):
        rows = self.mainWindow.window.tablePatient.rowCount()
        self.mainWindow.window.tablePatient.setRowCount(rows + 1)
        for j in range(len(rowData)):
            self.mainWindow.window.tablePatient.setItem(rows, j, QTableWidgetItem(rowData[j]))

    def addPatient(self):
        data = [
            self.mainWindow.window.lineEditSurname.text(),
            self.mainWindow.window.lineEditName.text(),
            self.mainWindow.window.lineEditPatronymic.text(),
            self.mainWindow.window.dateEdit.text()
        ]
        
        res = self.db.addPatient(data)
        if res:
            print("insert")
        else:
            print("no insert")
        self.fillTable()

    def startAnalyze(self):

        self.mainWindow.window.progressAnalyze.setFormat('Load model...')
        
        x1 = threading.Thread(target=self.analyze, args=(self.mainWindow.window.labelFilePath.text(),))
        x1.start()

    def changeProgressBar(self, item):
        item = item[0]

        data = {
            0 : 'Classify...',
            1 : 'Completed',
            2 : 'Classification error!',
            3 : 'Loading error!',
            4 : 'Loading error!'
        }

        if type(item) == int:
            self.mainWindow.window.progressAnalyze.setFormat(data[item])
        elif type(item) == str:
            self.mainWindow.window.textEditResult.setText('Lung cancer class: ' + item)
            self.mainWindow.window.tabWidget.setCurrentIndex(3)

    def analyze(self, filePath):
        loaded = self.mia.loadModel()

        if loaded:
            self.inProgress.emit([0])
            res = self.mia.classify(filePath)
            if len(res) > 0:
                self.inProgress.emit([1])
                self.inProgress.emit([res])
            else:
                self.inProgress.emit([2])
        else:
            self.inProgress.emit([3])

    def saveResults(self):
        cur = self.mainWindow.window.tablePatient.currentRow()
        data = [
            self.mainWindow.window.tablePatient.item(cur, 1).text(),
            self.mainWindow.window.textEditResult.toPlainText(),
            bytearray(0),
            self.image_to_byte_array()
        ]
        self.db.saveIn(data)

    def image_to_byte_array(self):
        try:
            with open(self.mainWindow.window.labelFilePath.text(), "rb") as image:
              f = image.read()
              b = bytearray(f)
              return b
        except Exception as e:
            logging.error(traceback.format_exc())
            return bytearray(0)