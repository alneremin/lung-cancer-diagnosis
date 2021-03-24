
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

    def authorize(self, user, password):
        query = QSqlQuery()
        query.exec(
          f"SELECT 1 FROM Users WHERE login=\'{user}\' AND password=\'{password}\'"
        )
        while query.next():
            query.finish()
            return True
        query.finish()
        return False
        

    def getPatients(self):
        data = []
        query = QSqlQuery()
        data_count = 6
        query.exec(
          "SELECT id, surname, name, patronym, date_of_birth, sex FROM Patient"
        )
        while query.next():
            data.append([str(query.value(i)) for i in range(data_count)]) 
            data[-1] = [" ".join(data[-1][1:3])] + data[-1]
        query.finish()

        return data

    def addPatient(self, data):

        query = QSqlQuery()
        res = query.exec(
            f"""
            INSERT INTO Patient (surname, name, patronym, date_of_birth, sex, address, phone_number, "next of kin", doctor)
            VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', 'm', '', '', '', '')
            """
        )
        return res

    def saveIn(self, data):
        query = QSqlQuery()
        insertQuery = f"""
                    INSERT INTO Analysis (patient, result, image_dcm, image_jpg)
                    VALUES (:patient, :result, :image_dcm, :image_jpg)
        """
        query.prepare(insertQuery)
        query.bindValue(":patient", data[0])
        query.bindValue(":result", data[1])
        query.bindValue(":image_dcm", data[2])
        query.bindValue(":image_jpg", data[3])
        query.exec()

        query.finish()
