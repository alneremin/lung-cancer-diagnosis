import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint,QSize
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import QMessageBox
from window.mainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.window.button_close.setText("{}".format('X'))
        self.window.button_info.setText("{}".format('?'))
        self.window.button_DownFile.setEnabled(False)
        self.window.tabWidget.setCurrentIndex(0)
        self.init_page_startAnaluyze()
        self.signal_button_clicked()

    def signal_button_clicked(self):
        self.window.button_close.clicked.connect(self.close_window)
        self.window.button_search.clicked.connect(self.search)

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
        
    def search(self):
        self.window.listPatient.addItem(self.window.lineEdit_search.text())

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
        self.window.listPatient.itemClicked.connect(self.selectionChanged)
        
    def selectionChanged(self, item):
        if item.text() == "test":
            #label
            self.window.label_surname.show()
            self.window.label_name.show()
            self.window.label_patronymic.show()
            self.window.label_date.show()
            self.window.label_gender.show()
            #info
            self.window.surname_patient.setText("Авдеев")
            self.window.surname_patient.show()
            self.window.name_patient.setText("Иван")
            self.window.name_patient.show()
            self.window.patronymic_patient.setText("Александрович")
            self.window.patronymic_patient.show()
            self.window.date_patient.setText("13.01.2000")
            self.window.date_patient.show()
            self.window.gender_patient.setText("мужской")
            self.window.gender_patient.show()
            self.window.button_DownFile.setEnabled(True)

    def close_window(self):
        reply = QMessageBox.question(self,
                                     "Message",                                     "Вы точно хотите закрыть приложение?",
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
