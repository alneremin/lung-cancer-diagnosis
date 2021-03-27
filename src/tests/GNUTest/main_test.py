
import sys

sys.path.insert(0, "../../")

import pytest

from pytestqt import qt_compat
from pytestqt.qt_compat import qt_api

import sys
import PyQt5
import PyQt5.QtCore as QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QSettings

from Controller.controller import MIAController
from Window.AuthorizationView import AuthorizationWindow
from Window.MainView import MainWindow
from Database.database import Database

from Window.mainWindow import Ui_MainWindow

"""
Тест №1 
Проверка названий надписей
"""
def test_main_labels(qtbot):

    mainWindow = QMainWindow()
    ui_MainWindow = Ui_MainWindow()

    ui_MainWindow.setupUi(mainWindow)

    qtbot.addWidget(mainWindow)

    mainWindow.setWindowTitle("M1")
    mainWindow.show()

    assert mainWindow.isVisible()
    assert mainWindow.windowTitle() == "M1"

    assert ui_MainWindow.labelSurname_2.text() == "Фамилия"
    assert ui_MainWindow.labelName_2.text() == "Имя"
    assert ui_MainWindow.labelPatronymic_2.text() == "Отчество"
    assert ui_MainWindow.labelDate.text() == "Дата рождения"
    assert ui_MainWindow.buttonForward.text() == "Далее"

"""
Тест №2 
Проверка работы перелистываний
"""
def test_main_pages(qtbot):

    mainWindow = QMainWindow()
    ui_MainWindow = Ui_MainWindow()

    ui_MainWindow.setupUi(mainWindow)

    #widget = HelloWidget()
    qtbot.addWidget(mainWindow)
    mainWindow.show()

    # первая страница
    ui_MainWindow.tabWidget.setCurrentIndex(0)
    assert ui_MainWindow.tabWidget.currentIndex() == 0
    assert ui_MainWindow.buttonAddPatient.isVisible()
    assert not ui_MainWindow.buttonStartAnalyze.isVisible()
    assert not ui_MainWindow.saveDB.isVisible()
    assert ui_MainWindow.lineEditSurname.text() == ''

    # вторая страница
    ui_MainWindow.tabWidget.setCurrentIndex(1)
    assert ui_MainWindow.tabWidget.currentIndex() == 1
    assert ui_MainWindow.plainTextEditAnalyze.isVisible()
    assert ui_MainWindow.progressAnalyze.isVisible()
    assert not ui_MainWindow.buttonAddPatientInDB.isVisible()

    # третья страница
    ui_MainWindow.tabWidget.setCurrentIndex(2)
    assert ui_MainWindow.tabWidget.currentIndex() == 2
    assert ui_MainWindow.textEditResult.isVisible()
    assert ui_MainWindow.saveDB.isVisible()
    assert ui_MainWindow.labelResult.isVisible()
    

"""
Тест №3 
Проверка работы полей добавления пациента
"""
def test_add_patient(qtbot):

    controller = MIAController(None, None)

    #authorizationWindow = AuthorizationWindow(db, controller)
    mainWindow = MainWindow(None, controller)

    qtbot.addWidget(mainWindow)
    mainWindow.show()

    mainWindow.window.tabWidget.setCurrentIndex(0)
    
    qtbot.mouseClick(mainWindow.window.buttonAddPatient, QtCore.Qt.LeftButton)
    assert mainWindow.window.tabWidget.currentIndex() == 3

    qtbot.keyPress(mainWindow.window.lineEditSurname, "a")
    qtbot.keyPress(mainWindow.window.lineEditSurname, "b")
    assert mainWindow.window.lineEditSurname.text() == "ab"

    mainWindow.window.lineEditSurname.clear()
    assert mainWindow.window.lineEditSurname.text() == ""

    assert not mainWindow.window.buttonBack.isVisible()
    assert not mainWindow.window.buttonForward.isVisible()

    qtbot.mouseClick(mainWindow.window.buttonCancelAddPatient, QtCore.Qt.LeftButton)
    assert mainWindow.window.tabWidget.currentIndex() == 0

    assert mainWindow.window.buttonBack.isVisible()
    assert mainWindow.window.buttonForward.isVisible()


"""
Тест №4
Проверка работы элементов на странице анализа
"""
def test_analyze(qtbot):

    controller = MIAController(None, None)

    #authorizationWindow = AuthorizationWindow(db, controller)
    mainWindow = MainWindow(None, controller)

    qtbot.addWidget(mainWindow)
    mainWindow.show()

    mainWindow.window.tabWidget.setCurrentIndex(0)
    
    
    mainWindow.addRowInTable(['Durak Ivan Ivanovich', '2', 'Durak', 'Ivan', 'Ivanovich', '20.10.1993', 'm'])
    item = mainWindow.window.tablePatient.item(0, 0)
    mainWindow.window.tablePatient.setCurrentItem(item)

    qtbot.mouseClick(mainWindow.window.buttonForward, QtCore.Qt.LeftButton)
    assert mainWindow.window.tabWidget.currentIndex() == 1

    assert mainWindow.window.labelFilePath.text() == 'Файл не открыт'
    assert mainWindow.window.progressAnalyze.value() == 0

    qtbot.mouseClick(mainWindow.window.buttonBack, QtCore.Qt.LeftButton)
    assert mainWindow.window.tabWidget.currentIndex() == 0

"""
Тест №5
Проверка работы элементов на странице результатов анализов
"""
def test_analyze_result(qtbot):

    controller = MIAController(None, None)

    #authorizationWindow = AuthorizationWindow(db, controller)
    mainWindow = MainWindow(None, controller)

    qtbot.addWidget(mainWindow)
    mainWindow.show()

    mainWindow.window.tabWidget.setCurrentIndex(0)
    
    
    mainWindow.addRowInTable(['Durak Ivan Ivanovich', '2', 'Durak', 'Ivan', 'Ivanovich', '20.10.1993', 'm'])
    item = mainWindow.window.tablePatient.item(0, 0)
    mainWindow.window.tablePatient.setCurrentItem(item)

    qtbot.mouseClick(mainWindow.window.buttonForward, QtCore.Qt.LeftButton)
    assert mainWindow.window.tabWidget.currentIndex() == 1
    qtbot.mouseClick(mainWindow.window.buttonForward, QtCore.Qt.LeftButton)
    assert mainWindow.window.tabWidget.currentIndex() == 2

    assert mainWindow.window.labelResult.text() == 'Результаты анализа'
    assert mainWindow.window.saveDB.text() == 'Cохранить в базу данных'

    qtbot.mouseClick(mainWindow.window.buttonForward, QtCore.Qt.LeftButton)
    assert mainWindow.window.tabWidget.currentIndex() == 0
