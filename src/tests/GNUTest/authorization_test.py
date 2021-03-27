
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
Проверка работы полей окна авторизации
"""
def test_authorization_window(qtbot):

    controller = MIAController(None, None)

    authorizationWindow = AuthorizationWindow(None, controller)
    #mainWindow = MainWindow(None, controller)

    qtbot.addWidget(authorizationWindow)
    authorizationWindow.show()

    assert authorizationWindow.window.label_3.text() == "Добро пожаловать"

    qtbot.keyPress(authorizationWindow.window.userName, "a")
    qtbot.keyPress(authorizationWindow.window.userName, "d")
    assert authorizationWindow.window.userName.text() == "ad"

    authorizationWindow.window.userName.clear()
    assert authorizationWindow.window.userName.text() == ""

    assert authorizationWindow.window.buttonEntrance.isVisible()
