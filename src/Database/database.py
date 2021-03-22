
import sys
import os
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox

class Database:
    def __init__(self, driver, path):
        self.db = None
        self.driver = driver
        self.path = path

    def createConnection(self):
        self.db = QSqlDatabase.addDatabase(self.driver)
        self.open()

    def open(self):
        self.db.setDatabaseName(self.path)
        if not self.db.open():
            QMessageBox.critical(
              None,
              "App Name - Error!",
              "Database Error: %s" % self.db.lastError().databaseText(),
            )
            return False
        return True

    def close(self):
        if self.db.isOpen():
            self.db.close()

    def findByName(self, name):
        data = []
        query = QSqlQuery()
        data_count = 6
        query.exec(
          f"SELECT id, surname, name, patronym, date_of_birth, sex FROM Patient WHERE surname= {name}"
        )
        ident, surname, name, patronym, date_of_birth, sex = range(data_count)
        while query.next():
            data.append([query.value(i) for i in range(data_count)])
        query.finish()
        return data

    def getPatients(self):
        data = []
        query = QSqlQuery()
        data_count = 6
        query.exec(
          "SELECT id, surname, name, patronym, date_of_birth, sex FROM Patient"
        )
        #ident, surname, name, patronym, date_of_birth, sex = range(data_count)
        while query.next():
            data.append([str(query.value(i)) for i in range(data_count)]) 
            data[-1] =  [" ".join(data[-1][1:3])] + data[-1]
        query.finish()
        return data