import sys
sys.path.insert(0, '../src')
import unittest
import datetime
from Database.database import Database
from PyQt5.QtCore import QSettings
from PyQt5.QtSql import QSqlDatabase

class TestDatabase(unittest.TestCase):
    
    """
            Тестирование функции addPatient()
    """            
    def testAddPatient(self):
        dbTestAddPatient = Database('QSQLITE', 'diagnostic.db')
        dbTestAddPatient.createConnection()
        
        data = ["Иванов", "Иванов", "Иванов", datetime.date(2000, 12, 13), 'm']
        res = dbTestAddPatient.addPatient(data)
        self.assertEqual(res, True)

        data = [13214, 213214, 41241241, datetime.date(2000, 12, 13), 'm']
        res = dbTestAddPatient.addPatient(data)
        self.assertEqual(res, True)
        
    """
            Тестирование функции authorize()
    """          
    def testAuthorize(self):
        dbTestAuthorize = Database('QSQLITE', 'diagnostic.db')
        dbTestAuthorize.createConnection()

        """
            Teст 1 авторизация администратора
        """        
        
        res = dbTestAuthorize.authorize("admin", "admin")
        self.assertEqual(res, True)

        """
            Teст 2 авторизация существующего пользователя
        """

        res = dbTestAuthorize.authorize("", "")
        self.assertEqual(res, True)

        """
            Teст 2 авторизация несуществующего пользователя
        """
        
        res = dbTestAuthorize.authorize("user", "12345")
        self.assertEqual(res, False)
        
    """
            Тестирование функции getPatients()
    """      
    def testGetPatients(self):
        dbTestGetPatients = Database('QSQLITE', 'diagnostic.db')
        dbTestGetPatients.createConnection()
        data = dbTestGetPatients.getPatients()
        len_data = len(data)
        data = ["Петрова", "Татьяна", "Петровна", datetime.date(1970, 2, 27), 'f']
        res = dbTestGetPatients.addPatient(data)
        data = dbTestGetPatients.getPatients()
        self.assertEqual(len(data), (len_data + 1))
        
    """
            Тестирование функции saveAnalyze()
    """        
    def testSaveAnalyze(self):
        dbTestGetPatients = Database('QSQLITE', 'diagnostic.db')
        dbTestGetPatients.createConnection()
        data = [
            1,
            'Lung cancer class: A',
            bytearray(0),
            bytearray(0)
        ]
        res = dbTestGetPatients.saveAnalyze(data)
        self.assertEqual(res, True)
        
    """
            Тестирование функции editPatient()
    """          
    def testEditPatient(self):
        dbtestEditPatient = Database('QSQLITE', 'diagnostic.db')
        res = dbtestEditPatient.createConnection()
        idPatient = 11
        dataNew = ["Иванов", "Иван", "Иванович", datetime.date(1979, 3, 11), 'm']
        dataOld = dbtestEditPatient.getPatient(idPatient)
        dbtestEditPatient.editPatient(dataNew, idPatient)
        data = dbtestEditPatient.getPatient(idPatient)
        res = True
        check = ["Иванов", "Иван", "Иванович", str(datetime.date(1979, 3, 11)), 'm']
        i = 0
        for element in data:
            if data[i] != check[i]:
                res = False
                break
            i += 1
        
        self.assertEqual(res, True)
        dbtestEditPatient.close()
        
    """
            Тестирование функции removePatient()
    """   
    def testRemovePatient(self):
        dbTestRemovePatient = Database('QSQLITE', 'diagnostic.db')
        res = dbTestRemovePatient.createConnection()
        data = dbTestRemovePatient.getPatients()
        len_data = len(data)

        res = dbTestRemovePatient.removePatient(999999)

        self.assertEqual(res, True)
        dbTestRemovePatient.close()
        

    """
            Тестирование функции createConnection()
    """
    def testOpen(self):
        """
            Teст 1 попытка открыть существующую базу данных
        """
        dbTestOpen1 = Database('QSQLITE', 'diagnostic.db')
        res = dbTestOpen1.createConnection()
        self.assertEqual(res, True)
        dbTestOpen1.close()
        """
            Teст 2 попытка открыть несуществующую базу данных
        """
        dbTestOpen2 = Database('QSQLITE', 'diagnostdwadawic.db')
        res = dbTestOpen2.createConnection()
        self.assertEqual(res, False)
        dbTestOpen2.close()



if __name__ == "__main__":
    unittest.main()
