from PyQt5 import  QtCore, QtGui, QtWidgets
from Window.mainWindow import MainWindow
from ui.authorizationWindow import Ui_AuthWindow

class AuthWindow(QtWidgets.QMainWindow):
    window: Ui_AuthWindow
    mainWindow: MainWindow

    def __init__(self):
        super(AuthWindow, self).__init__()
        self.mainWindow = MainWindow()
        self.mainWindow.__init__()
        self.window = Ui_AuthWindow()
        self.window.setupUi(self)

        self.mainWindow.window.buttonAnalysis.setVisible(False)
        self.mainWindow.window.editResult.setVisible(False)
        self.mainWindow.window.saveResult.setVisible(False)

        self.start()

    def start(self):
        self.window.buttonAuth.clicked.connect(self.authorization)
        self.mainWindow.window.exit.clicked.connect(self.exit)
        self.mainWindow.window.buttonDateEntryFile.clicked.connect(self.dateEntryFile)
        self.mainWindow.window.buttonInput.clicked.connect(self.entryFile)
        self.mainWindow.window.buttonSearchPatientAnalyse.clicked.connect(self.searchPatient)
        self.mainWindow.window.buttonAnalysis.clicked.connect(self.analyse)
        self.mainWindow.window.saveResult.clicked.connect(self.saveResult)

    # сохранение результата после анализа
    def saveResult(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "", "*.txt")
        my_file = open(file_path, 'w')
        my_file.write(self.mainWindow.window.editResult.toPlainText())
        my_file.close()
    # анализ
    def analyse(self):
        # тож пока заглушка
        self.mainWindow.window.editResult.setVisible(True)
        self.mainWindow.window.saveResult.setVisible(True)

    # Поиск пациента
    def searchPatient(self):
        # пока заглушка. нужна бд
        self.mainWindow.window.buttonAnalysis.setVisible(True)

    # Выход
    def exit(self):
        self.mainWindow.window.User.setText(self.window.editUserName.clear())
        self.mainWindow.close()
        self.show()


    # Ввод данных
    def entryFile(self):
        Name = self.mainWindow.window.lineEditName.text()
        Surname = self.mainWindow.window.lineEditSurname.text()
        Patronymic = self.mainWindow.window.lineEditPatronymic.text()
        BirthDate = self.mainWindow.window.dateEdit.text()
        if len(Name) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Поле \"Имя\" не должно быть пустым")
        elif len(Surname) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Поле \"Фамилия\" не должно быть пустым")
        elif len(Patronymic) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Поле \"Отчество\" не должно быть пустым")
        else:
            QtWidgets.QMessageBox.about(self, "Инфо", "Данные сохранены")

    def dateEntryFile(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "", "*.dcm")

    # Авторизация
    def authorization(self):
        UserName = self.window.userName.text()
        UserPassword = self.window.userPassword.text()
        if(len(UserName) == 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Поле \"Пользователь\" не должно быть пустым")
        elif(len(UserPassword) == 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Поле \"Пароль\" не должно быть пустым")
        else:
            # Тут нужно добавить проверки с бд на пользователя
            self.mainWindow.window.User.setText(UserName)
            self.mainWindow.show()
            self.close()
