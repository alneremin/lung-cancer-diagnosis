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
        self.init_tables()
        self.window.tabBar.hide()
        self.window.button_close.setText("{}".format('X'))
        self.window.button_info.setText("{}".format('?'))
        self.window.button_DownFile.setEnabled(False)
        self.window.tabWidget.setCurrentIndex(0)
        self.init_page_startAnaluyze()

        self.signal_button_clicked()
        self.window.button_search.setEnabled(False)
        #self.window.button_search.clicked.connect(self.search)
        self.window.lineEdit_search.textChanged.connect(self.search)
        self.window.tablePatient.clicked.connect(self.selectionChanged)
    
    def init_tables(self):
        #self.window.tablePatient = QTableWidget()
        self.window.tablePatient.setColumnCount(7)
        self.window.tablePatient.setHorizontalHeaderLabels(["fullname", "id", "surname", "name", "patronym", "date_of_birth", "sex"])
        self.window.tablePatient.horizontalHeader().hide()
        for i in range(1,7):
            self.window.tablePatient.setColumnHidden(i, True)

    def signal_button_clicked(self):
        self.window.button_close.clicked.connect(self.close_window)

        #back
        self.window.index4_button_back.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(0))
        self.window.index3_button_back.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(2))
        self.window.index2_button_back.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(1))
        self.window.index1_button_back.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(0))
        #go tab
        self.window.button_AddPatient.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(4))
        self.window.button_Analyze.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(2))
        self.window.button_DownFile.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(1))
        self.window.button_Result.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(3))

        self.window.button_load_file.clicked.connect(self.load_file)
        
    def init_page_startAnaluyze(self):
        #label
        self.window.label_surname.hide()
        self.window.label_name.hide()
        self.window.label_patronymic.hide()
        self.window.label_date.hide()
        self.window.label_gender.hide()
        #info
        self.window.surname_patient.hide()
        self.window.name_patient.hide()
        self.window.patronymic_patient.hide()
        self.window.date_patient.hide()
        self.window.gender_patient.hide()
        
    def selectionChanged(self, item):
        
        if item.row() != -1:
            items = [
                self.window.tablePatient.item(item.row(), i).text() for i in range(self.window.tablePatient.columnCount())
            ]
            self.window.label_surname.show()
            self.window.label_name.show()
            self.window.label_patronymic.show()
            self.window.label_date.show()
            self.window.label_gender.show()
            #info
            self.window.surname_patient.setText(items[2])
            self.window.surname_patient.show()
            self.window.name_patient.setText(items[3])
            self.window.name_patient.show()
            self.window.patronymic_patient.setText(items[4])
            self.window.patronymic_patient.show()
            self.window.date_patient.setText(items[5])
            self.window.date_patient.show()
            self.window.gender_patient.setText(items[6])
            self.window.gender_patient.show()
            self.window.button_DownFile.setEnabled(True)

    def search(self):
        for i in range(self.window.tablePatient.rowCount()):
            search_text = str.lower(self.window.lineEdit_search.text())
            patient_name = str.lower(self.window.tablePatient.item(i, 0).text())
            
            if search_text in patient_name:
                self.window.tablePatient.showRow(i)
            else:
                self.window.tablePatient.hideRow(i)

    def close_window(self):
        reply = QMessageBox.question(self,
                                     "Message",                                     "Вы точно хотите закрыть приложение?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QtWidgets.QApplication.quit()
        else:
            pass

    def load_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"Image files (*.jpg *.dcm *.png)")
        self.window.label_file_path.setText(fname[0])

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = QPoint()

    def mouseMoveEvent(self, event):
        if not self.__press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.__press_pos))
