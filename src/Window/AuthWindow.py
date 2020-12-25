import time

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.mainWindow import MainWindow
from ui.authorizationWindow import Ui_AuthWindow
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class AuthWindow(QtWidgets.QMainWindow):
    window: Ui_AuthWindow
    mainWindow: MainWindow

    def __init__(self):
        super(AuthWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.mainWindow = MainWindow()
        self.mainWindow.__init__()
        self.window = Ui_AuthWindow()
        self.window.setupUi(self)
        self.mainWindow.window.tabWidget.tabBar().setEnabled(False)
        self.start()

    def start(self):
        # переход м/у cтраницами
        self.mainWindow.window.buttonAddPatient.clicked.connect(self.show_add_patient)
        self.mainWindow.window.buttonDownFile.clicked.connect(self.show_download_file)
        self.mainWindow.window.buttonAnalyze.clicked.connect(self.show_analyze)
        self.mainWindow.window.buttonResult.clicked.connect(self.show_result_analyze)

        # возврат на прошлую страницу
        self.mainWindow.window.Index1buttonBack.clicked.connect(self.go_back_to_page_index_0)
        self.mainWindow.window.Index2buttonBack.clicked.connect(self.go_back_to_page_index_1)
        self.mainWindow.window.Index3buttonBack.clicked.connect(self.go_back_to_page_index_2)
        self.mainWindow.window.Index4buttonBack.clicked.connect(self.go_back_to_page_index_0)

        # выход + авторизация
        self.window.buttonExit.clicked.connect(self.authorization)
        self.mainWindow.window.exit.clicked.connect(self.exit)

        # анализ
        self.mainWindow.window.buttonStartAnalyze.clicked.connect(self.start_analyze)
        #Работа с файлами
        self.mainWindow.window.buttonDownloadCTFile.clicked.connect(self.open_file)
        self.mainWindow.window.saveBD.clicked.connect(self.save_result_to_the_database)

    def start_analyze(self):
        i = 0
        self.mainWindow.window.progressAnalyze.setValue(i)
        i = 100
        self.mainWindow.window.progressAnalyze.setValue(i)
        self.mainWindow.window.buttonResult.setEnabled(True)

    def open_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", '', '(* .zip)')
        self.mainWindow.window.labelFilePath.setText(file_path)
        print("файл загружен")
    def save_result_to_the_database(self):
        QtWidgets.QMessageBox.information(self, "Сохранение", "Данные успешно сохранены")
        print("сохраняю")

    def exit(self):
        self.mainWindow.close()
        self.show()

    def go_back_to_page_index_0(self) -> None:
        self.mainWindow.window.tabWidget.setCurrentIndex(0)

    def go_back_to_page_index_1(self) -> None:
        self.mainWindow.window.tabWidget.setCurrentIndex(1)

    def go_back_to_page_index_2(self) -> None:
        self.mainWindow.window.tabWidget.setCurrentIndex(2)

    def show_download_file(self) -> None:
        self.mainWindow.window.tabWidget.setCurrentIndex(1)

    def show_analyze(self) -> None:
        self.mainWindow.window.buttonResult.setEnabled(False)
        self.mainWindow.window.tabWidget.setCurrentIndex(2)

    def show_result_analyze(self) -> None:
        self.mainWindow.window.tabWidget.setCurrentIndex(3)

    def show_add_patient(self) -> None:
        self.mainWindow.window.tabWidget.setCurrentIndex(4)

    def authorization(self):
        user_name = self.window.userName.text()
        user_password = self.window.userPassword.text()
        if len(user_name) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Поле \"Имя\" не должно быть пустым")
        elif len(user_password) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Поле \"Пароль\" не должно быть пустым")
        else:
            self.mainWindow.window.tabWidget.setCurrentIndex(0)
            self.mainWindow.window.User.setText(user_name)
            self.mainWindow.show()
            self.close()
