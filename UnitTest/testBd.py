import sys
sys.path.insert(0, '../src')
import unittest
import datetime
from Database.database import Database
from PyQt5.QtCore import QSettings
from PyQt5.QtSql import QSqlDatabase

class TestCalculator(unittest.TestCase):
        
    def testAddPatient(self):
        self.dbTestAddPatient = Database('QSQLITE', 'diagnostic.db')
        self.dbTestAddPatient.createConnection()
        data = ["Иванов", "Иванов", "Иванов", datetime.date(2000, 12, 13), 'm']
        res = self.dbTestAddPatient.addPatient(data)
        self.assertEqual(res, True)

        data = [13214, 213214, 41241241, datetime.date(2000, 12, 13), 'm']
        res = self.dbTestAddPatient.addPatient(data)
        self.assertEqual(res, True)
        
        data = ["Петрова", "Татьяна", "Петровна", datetime.date(1970, 2, 27), 'f']
        res = self.dbTestAddPatient.addPatient(data)
        self.assertEqual(res, True)

        data = ["Иванов", "Иванов", "Иванов", datetime.date(2000, 12, 13), 'm']
        res = self.dbTestAddPatient.addPatient(data)
        self.assertEqual(res, True)

    def testAuthorize(self):
        self.dbTestAuthorize = Database('QSQLITE', 'diagnostic.db')
        self.dbTestAuthorize.createConnection()
        res = self.dbTestAuthorize.authorize("admin", "admin")
        self.assertEqual(res, True)

        res = self.dbTestAuthorize.authorize("admin", "admin")
        self.assertEqual(res, True)

        res = self.dbTestAuthorize.authorize("", "")
        self.assertEqual(res, True)

        res = self.dbTestAuthorize.authorize("user", "12345")
        self.assertEqual(res, False)

    def testGetPatients(self):
        self.dbTestGetPatients = Database('QSQLITE', 'diagnostic.db')
        self.dbTestGetPatients.createConnection()
        data = self.dbTestGetPatients.getPatients()
        len_data = len(data)
        data = ["Петрова", "Татьяна", "Петровна", datetime.date(1970, 2, 27), 'f']
        res = self.dbTestGetPatients.addPatient(data)
        data = self.dbTestGetPatients.getPatients()
        self.assertEqual(len(data), (len_data + 1))

    def testSaveIn(self):
        self.dbTestGetPatients = Database('QSQLITE', 'diagnostic.db')
        self.dbTestGetPatients.createConnection()
        data = [
            1,
            'Lung cancer class: A',
            bytearray(0),
            bytearray(0)
        ]
        res = self.dbTestGetPatients.saveIn(data)
        self.assertEqual(res, True)
        

    def testOpen(self):
        self.dbTestOpen1 = Database('QSQLITE', 'diagnostic.db')
        res = self.dbTestOpen1.createConnection()
        self.assertEqual(res, True)
        self.dbTestOpen1.close()

        self.dbTestOpen2 = Database('QSQLITE', 'diagnostdwadawic.db')
        res = self.dbTestOpen2.createConnection()
        self.assertEqual(res, False)
        self.dbTestOpen2.close()



if __name__ == "__main__":
    unittest.main()
