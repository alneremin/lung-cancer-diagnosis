import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings

from Controller.controller import MIAController
from Window.AuthorizationView import AuthorizationWindow
from Window.MainView import MainWindow
from Database.database import Database

import logging
import logging.config

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)

logger = logging.getLogger('log02')

if __name__ == "__main__":

    app = QApplication([])

    settings = QSettings('settings.conf', QSettings.IniFormat)
    settings.setIniCodec("UTF-8")
    
    db = Database(settings.value('driver'), settings.value('db_path'))
    if not db.createConnection():
        sys.exit(1)

    networkPath = settings.value('model_path')
    controller = MIAController(db, networkPath)

    authorizationWindow = AuthorizationWindow(db, controller)
    mainWindow = MainWindow(db, controller)
    

    sys.exit(app.exec())
