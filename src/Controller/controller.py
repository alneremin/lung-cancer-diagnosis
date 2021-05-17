from PyQt5.QtCore import QObject, pyqtSignal

from MIA.mia import MIA
import threading
import logging

logger = logging.getLogger('log02')

class MIAController(QObject):
    def __init__(self, model, networkPath):
        super(MIAController, self).__init__()
        self.model = model
        self.mia = MIA(networkPath)
        self.views = {}

    inProgress = pyqtSignal(list)

    def setView(self, view, name):
        self.views[name] = view

    def exit(self):
        if self.views['MainWindow'].close():
            self.views['AuthorizationWindow'].show()


    def startWork(self, user):
        self.views['AuthorizationWindow'].close()
        self.views['MainWindow'].setWindowTitle(user + ": Система меддиагностики")
        self.connectWithMainWindow()
        self.views['MainWindow'].fillTable()
        self.views['MainWindow'].show()

    def connectWithMainWindow(self):
        # при нажатии на "Сохранить в БД" вызываем saveResults
        self.views['MainWindow'].window.saveDB.clicked.connect(self.saveResults)
        
        # реагируем на все изменения в течение работы анализатора 
        self.inProgress.connect(self.views['MainWindow'].changeProgressBar)

    """
        # РАБОТА НЕЙРОСЕТИ
    """

    def startAnalyze(self, filePath):
        self.mia.work = True
        logger.info("Запускается поток для анализа для работы нейросети")
        x1 = threading.Thread(target=self.analyze, args=(filePath,))
        x1.start()

    def analyze(self, filePath):
        
        segm_is_loaded = self.mia.loadSegmentationModel()
        self.inProgress.emit([4])
        if segm_is_loaded:
            
            clf_is_loaded = self.mia.loadClassificationModel()
            self.inProgress.emit([0])
            segmentated, segment_img, newFilePath = self.mia.segmentify(filePath)
            if segmentated and segm_is_loaded:
                classifed, result = self.mia.classify(newFilePath)
                if classifed:
                    self.inProgress.emit([1])
                    self.inProgress.emit([[result, segment_img]])
                else:
                    self.inProgress.emit([2])
            else:
                self.inProgress.emit([3])
        else:
            self.inProgress.emit([5])

        self.mia.work = False

    """
        # РАБОТА С МОДЕЛЬЮ ДАННЫХ (БД)
    """

    def addPatient(self, _id=None):
        data = self.views['MainWindow'].getNewPatientData()
        if _id is None:
            res = self.model.addPatient(data)
        else:
            res = self.model.editPatient(data, _id)
        self.views['MainWindow'].fillTable()

    def saveResults(self):
        data = self.views['MainWindow'].getResultData()
        isSaved = self.model.saveAnalyze(data)
        self.views['MainWindow'].dataIsSaved(isSaved)

    def removePatient(self, _id):
        return self.model.removePatient(_id)

    """
        # etc
    """

    def image_to_byte_array(self, path):
        try:
            with open(path, "rb") as image:
              f = image.read()
              b = bytearray(f)
              return b
        except Exception as e:
            logger.exception('Не удалось сохранить в битовом формате файл: %s', path)
            return bytearray(0)