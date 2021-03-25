import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint,QSize
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QFileDialog
)
from Window.mainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.initTables()
        #self.window.tabBar.hide()
        #self.window.buttonClose.setText("{}".format('X'))
        #self.window.buttonInfo.setText("{}".format('?'))
        #self.window.buttonDownFile.setEnabled(False)
        self.window.tabWidget.setCurrentIndex(0)
        self.initPageStartAnalyze()
        self.initSignalsWhenButtonClicked()
        #self.window.buttonSearch.setEnabled(False)
        #self.window.button_search.clicked.connect(self.search)
        self.window.lineEditSearch.textChanged.connect(self.search)
        self.window.tablePatient.selectionModel().currentChanged.connect(self.selectionChanged)
    
    def initTables(self):
        #self.window.tablePatient = QTableWidget()
        self.window.tablePatient.setColumnCount(7)
        self.window.tablePatient.setHorizontalHeaderLabels(["fullname", "id", "surname", "name", "patronym", "date_of_birth", "sex"])
        self.window.tablePatient.horizontalHeader().hide()
        for i in range(1,7):
            self.window.tablePatient.setColumnHidden(i, True)

    def initSignalsWhenButtonClicked(self):
        pass
        #self.window.buttonClose.clicked.connect(self.closeWindow)

        #back
        #self.window.index4ButtonBack.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(0))
        #self.window.index3ButtonBack.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(2))
        #self.window.index2ButtonBack.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(1))
        #self.window.index1ButtonBack.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(0))
        #go tab
        self.window.buttonAddPatient.clicked.connect(self.openAddPatientPage)
        #self.window.buttonAnalyze.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(2))
        #self.window.buttonDownFile.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(1))
        #self.window.buttonResult.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(3))
        self.window.buttonForward.clicked.connect(self.forward)
        self.window.buttonBack.clicked.connect(self.back)
        #self.window.buttonLoadFile.clicked.connect(self.loadFile)
    def forward(self):
        if self.window.tabWidget.currentIndex() < self.window.tabWidget.count() - 2:
            self.window.tabWidget.setCurrentIndex(self.window.tabWidget.currentIndex() + 1)

    def back(self):
        if self.window.tabWidget.currentIndex() > 0:
            self.window.tabWidget.setCurrentIndex(self.window.tabWidget.currentIndex() - 1)

    def openAddPatientPage(self):
        self.window.buttonBack.setVisible(False)
        self.window.buttonForward.setVisible(False)
        self.window.tabWidget.setCurrentIndex(3)

    def completePatientAdding(self):
        self.window.buttonBack.setVisible(True)
        self.window.buttonForward.setVisible(True)
        self.window.tabWidget.setCurrentIndex(0)

        self.window.lineEditSurname.clear(),
        self.window.lineEditName.clear(),
        self.window.lineEditPatronymic.clear(),
        self.window.dateEdit.clear(),
        self.window.radioButtonMale.setChecked(True)

    def initPageStartAnalyze(self):
        pass
        """
        #label
        self.window.labelSurname_2.hide()
        self.window.labelName_2.hide()
        self.window.labelPatronymic_2.hide()
        self.window.labelDate.hide()
        self.window.labelGender.hide()
        #info
        self.window.surnamePatient.hide()
        self.window.namePatient.hide()
        self.window.patronymicPatient.hide()
        self.window.datePatient.hide()
        self.window.genderPatient.hide()
        """
        
    def selectionChanged(self, item):
        
        if item.row() != -1:
            items = [
                self.window.tablePatient.item(item.row(), i).text() for i in range(self.window.tablePatient.columnCount())
            ]
            
            #label
            self.window.labelSurname_2.show()
            self.window.labelName_2.show()
            self.window.labelPatronymic_2.show()
            self.window.labelDate.show()
            self.window.labelGender.show()
            #info
            self.window.surnamePatient.show()
            self.window.namePatient.show()
            self.window.patronymicPatient.show()
            self.window.datePatient.show()
            self.window.genderPatient.show()
            
            self.window.surnamePatient.setText(items[2])
            self.window.namePatient.setText(items[3])
            self.window.patronymicPatient.setText(items[4])
            self.window.datePatient.setText(items[5])
            self.window.genderPatient.setText(items[6])

            #self.window.buttonDownFile.setEnabled(True)

    def search(self):
        for i in range(self.window.tablePatient.rowCount()):
            searchText = str.lower(self.window.lineEditSearch.text())
            patientName = str.lower(self.window.tablePatient.item(i, 0).text())
            
            if searchText in patientName:
                self.window.tablePatient.showRow(i)
            else:
                self.window.tablePatient.hideRow(i)

    def closeWindow(self):
        reply = QMessageBox.question(self,
                                     "Message",                                     "Вы точно хотите закрыть приложение?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QtWidgets.QApplication.quit()
        else:
            pass

    def loadFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"Image files (*.jpg *.dcm *.png)")
        self.window.labelFilePath.setText(fname[0])

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = QPoint()

    def mouseMoveEvent(self, event):
        if not self.__press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.__press_pos))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and self.window.tabWidget.currentIndex() == 0:
            self.window.tabWidget.setCurrentIndex(1)
        event.accept()