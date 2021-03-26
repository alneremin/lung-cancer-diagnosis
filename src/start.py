import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings

from Controller.controller import MIAController
from Window.AuthorizationView import AuthorizationWindow
from Window.MainView import MainWindow
from Database.database import Database


if __name__ == "__main__":
    app = QApplication([])

    settings = QSettings('settings.conf', QSettings.IniFormat)
    settings.setIniCodec("UTF-8")
    
    db = Database(settings.value('driver'), settings.value('db_path'))
    db.createConnection()

    networkPath = settings.value('model_path')
    controller = MIAController(db, networkPath)

    authorizationWindow = AuthorizationWindow(db, controller)
    mainWindow = MainWindow(db, controller)
    

    sys.exit(app.exec())
