
import sys
import os
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QFile

import logging

logger = logging.getLogger('log02')

class Database:
    def __init__(self, driver, path):
        self.db = None
        self.driver = driver
        self.path = path

    def createConnection(self):
        self.db = QSqlDatabase.addDatabase(self.driver)
        return self.open()

    def open(self):
        self.db.setDatabaseName(self.path)
        if not QFile(self.path).exists():
            logger.error('Database file doesn\'t exists: %s', self.path)
            return False
        """
        QMessageBox.critical(
              None,
              "App Name - Error!",
              "Database Error: %s" % self.db.lastError().databaseText(),
            )
        """
        isOpened = self.db.open()
        if not isOpened:
            logger.error("Database Error: %s", self.db.lastError().databaseText())
        return isOpened

    def close(self):
        if self.db.isOpen():
            self.db.close()

    def authorize(self, user, password):
        query = QSqlQuery()
        query.exec(
          f"SELECT 1 FROM Users WHERE login=\'{user}\' AND password=\'{password}\'"
        )
        while query.next():
            query.finish()
            return True
        query.finish()
        logger.warning("Не удалось найти записи в БД для авторизации")
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
            VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '', '', '', '')
            """
        )
        if not res:
            logger.error("Database Error: %s", self.db.lastError().databaseText())
        return res

    def editPatient(self, data, id):

        query = QSqlQuery()
        res = query.exec(
            f"""
            UPDATE Patient SET surname='{data[0]}', name='{data[1]}', patronym='{data[2]}', date_of_birth='{data[3]}', sex='{data[4]}'
            WHERE id={id}
            """
        )
        if not res:
            logger.error("Database Error: %s", self.db.lastError().databaseText())
        return res

    def getPatient(self, _id):
        data = []
        query = QSqlQuery()
        data_count = 5
        sql = "SELECT surname, name, patronym, date_of_birth, sex FROM Patient WHERE id =" + str(_id)
        res = query.exec(sql)
        while query.next():
            data.append([str(query.value(i)) for i in range(data_count)])
        query.finish()
        return data[0]
        
    def removePatient(self, _id):

        #id = str(id)
        print(_id)
        query = QSqlQuery()
        res = query.exec(
            f"""
            DELETE FROM Patient WHERE id={_id}
            """
        )
        if not res:
            logger.error("Database Error: %s", self.db.lastError().databaseText())
        return res

    def saveAnalyze(self, data):
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
        res = query.exec()
        if not res:
            logger.error("Database Error: %s", self.db.lastError().databaseText())

        query.finish()
        return res

    def __del__(self):
        self.close()
