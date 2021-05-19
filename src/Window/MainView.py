import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint, QSize, QDate
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QFileDialog
)
from Window.mainWindow import Ui_MainWindow
from Window.mpl import MplCanvas
import SimpleITK as sitk
from datetime import datetime
import logging

class Result():
    def __init__(self, data):
        self.imgClass = data[0]
        self.segmentatedImg = data[1]
        self.tumorBorders = data[2]
        self.pathToInitImg = data[3]

logger = logging.getLogger('log02')

class MainWindow(QtWidgets.QMainWindow): # Ui_MainWindow
    def __init__(self, model, controller):
        super(self.__class__, self).__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.resultData = None
        self.model = model
        self.controller = controller
        self.controller.setView(self, 'MainWindow')

        self.initAll()

    def initAll(self):

        # инициализируем таблицу - заполняем ее данными из БД
        self.initTables()

        # делаем первую страницу стартовой
        self.window.tabWidget.setCurrentIndex(0)

        # соединяем слоты с сигналами 
        self.connectSignalsWithSlots()

        # нарисуем график и добавим его в QHBoxLayout
        self.canvas = MplCanvas()      
        self.window.horizontalLayout_7.addWidget(self.canvas)

    def connectSignalsWithSlots(self):

        # при нажатии на кнопку "Добавить пациента" переходим на страницу добавления
        self.window.buttonAddPatient.clicked.connect(self.openAddPatientPage)

        # при нажатии на кнопку "Изменить пациента" переходим на страницу изменения
        self.window.buttonEditPatient.clicked.connect(self.openEditPatientPage)

        # при нажатии на кнопку "Удалить" удаляем данные о пациенте
        self.window.buttonDeletePatient.clicked.connect(self.removePatient)
        
        # при нажатии на кнопку "Далее" перелистываем страницу ->
        self.window.buttonForward.clicked.connect(self.forward)
        # при нажатии на кнопку "Назад" перелистываем страницу <-
        self.window.buttonBack.clicked.connect(self.back)
        # при изменении текста ищем совпадения
        self.window.lineEditSearch.textChanged.connect(self.search)
        # при изменении текущей ячейки меняем и данные правой части стартовой страницы
        self.window.tablePatient.selectionModel().currentChanged.connect(self.selectionChanged)

        # при нажатии на кнопку "Создать пациента" добавляем его в БД
        self.window.buttonAddPatientInDB.clicked.connect(self.addPatient)

        # при переходе со страницы Добавления пациента вызываем метод completePatientAdding
        self.window.buttonAddPatientInDB.clicked.connect(self.completePatientAdding)
        self.window.buttonCancelAddPatient.clicked.connect(self.completePatientAdding)

        # при нажатии на "Анализ" начинаем анализ данных
        self.window.buttonStartAnalyze.clicked.connect(self.startAnalyze)

        # ставим обработчик триггеров верхнего меню
        self.window.menuBar.triggered.connect(self.menuTriggered)


    def forward(self):
        if self.window.tabWidget.currentIndex() == 0 and self.window.tablePatient.currentRow() < 0:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Уведомление")
            msgBox.setText("Выберите пациента!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setDefaultButton(QMessageBox.Ok)

            msgBox.exec()
            return

        if self.window.tabWidget.currentIndex() < self.window.tabWidget.count() - 2:
            self.window.tabWidget.setCurrentIndex(self.window.tabWidget.currentIndex() + 1)
        else:
            self.window.tabWidget.setCurrentIndex(0)

    def back(self):
        if self.window.tabWidget.currentIndex() > 0:
            self.window.tabWidget.setCurrentIndex(self.window.tabWidget.currentIndex() - 1)


    def menuTriggered(self, action):
        actions = {
            'Загрузить снимок': self.loadFile,
            'Загрузить пациента': self.loadPatient,
            'Выйти': self.controller.exit,
            'О программе': self.aboutProgram
        }
        try:
            actions[action.text()]()
        except:
            logger.exception('Не удалось найти пункт верхнего меню: %s', action.text())


    def loadPatient(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"Image files (*.dcm)")
        if fname[0] != "":
            try:
                img = sitk.ReadImage(fname[0])
                for i in img.GetMetaDataKeys():
                    print(i, img.GetMetaData(i))
            except Exception:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Ошибка!")

                msgBox.setText("Не удалось открыть данные.")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setDefaultButton(QMessageBox.Ok)
                msgBox.exec()

    """
        # Работа с таблицей tablePatient
    """

    def initTables(self):
        self.window.tablePatient.setColumnCount(7)
        self.window.tablePatient.setHorizontalHeaderLabels(["fullname", "id", "surname", "name", "patronym", "date_of_birth", "sex"])
        self.window.tablePatient.horizontalHeader().hide()
        for i in range(1,7):
            self.window.tablePatient.setColumnHidden(i, True)


    def fillTable(self):
        data = self.model.getPatients()
        #currentRow = self.mainWindow.window.tablePatient.currentRow()
        self.window.tablePatient.setRowCount(0)
        for row in data:
            self.addRowInTable(row)

        item = self.window.tablePatient.item(0, 0)
        self.window.tablePatient.setCurrentItem(item)
        self.selectionChanged(item)
            #self.mainWindow.window.tablePatient.insertRow(self.mainWindow.window.tablePatient.rowCount())
            #model = self.mainWindow.window.tablePatient.selectionModel()
            #model.insertRow(0)#.addItem(" ".join(row[1:4]))
        #self.mainWindow.window.tablePatient.setCurrentCell(currentRow, 0)

    def addRowInTable(self, rowData):
        rows = self.window.tablePatient.rowCount()
        self.window.tablePatient.setRowCount(rows + 1)
        for j in range(len(rowData)):
            self.window.tablePatient.setItem(rows, j, QTableWidgetItem(str.strip(rowData[j])))


    def search(self):
        for i in range(self.window.tablePatient.rowCount()):
            searchText = str.lower(self.window.lineEditSearch.text())
            patientName = str.lower(self.window.tablePatient.item(i, 0).text())
            
            if searchText in patientName:
                self.window.tablePatient.showRow(i)
            else:
                self.window.tablePatient.hideRow(i)

    def selectionChanged(self, item):
        
        if item.row() != -1:
            items = [
                self.window.tablePatient.item(item.row(), i).text() for i in range(2, self.window.tablePatient.columnCount())
            ]
            
            self.window.surnamePatient.setText(items[0])
            self.window.namePatient.setText(items[1])
            self.window.patronymicPatient.setText(items[2])
            self.window.datePatient.setText(items[3])
            self.window.genderPatient.setText(items[4])

            #self.window.buttonDownFile.setEnabled(True)

    """
        # Добавление пациента
    """

    def getNewPatientData(self):
        return [
            self.window.lineEditSurname.text(),
            self.window.lineEditName.text(),
            self.window.lineEditPatronymic.text(),
            self.window.dateEdit.text(),
            'm' if self.window.radioButtonMale.isChecked() else 'f'
        ]

    def openAddPatientPage(self):
        self.window.buttonBack.setVisible(False)
        self.window.buttonForward.setVisible(False)
        self.window.buttonAddPatientInDB.setText('Добавить')
        self.window.tabWidget.setCurrentIndex(3)

    def completePatientAdding(self):
        self.window.buttonBack.setVisible(True)
        self.window.buttonForward.setVisible(True)
        self.window.tabWidget.setCurrentIndex(0)

        self.window.lineEditSurname.clear(),
        self.window.lineEditName.clear(),
        self.window.lineEditPatronymic.clear(),
        self.window.dateEdit.clear(),
        self.window.radioButtonMale.setChecked(True)
    
    def addPatient(self):
        params = {
            'Добавить': [],
            'Изменить': [self.window.tablePatient.item(self.window.tablePatient.currentRow(), 1).text()]
        }
        self.controller.addPatient(*params[self.window.buttonAddPatientInDB.text()])

    """
        # Релактирование данных о пациенте
    """

    def openEditPatientPage(self):

        if self.window.tablePatient.currentRow() == -1:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Внимание")
            msgBox.setText("Выберите пациента")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.exec()
            return

        self.window.lineEditSurname.setText(self.window.surnamePatient.text())
        self.window.lineEditName.setText(self.window.namePatient.text())
        self.window.lineEditPatronymic.setText(self.window.patronymicPatient.text())
        self.window.dateEdit.setDate(QDate.fromString(self.window.datePatient.text(), 'dd.MM.yyyy'))
        #if self.window.genderPatient.text() == 'm':
        self.window.radioButtonMale.setChecked(self.window.genderPatient.text() == 'm')
        #else:
        #    self.window.radioButtonFemale.setChecked(True)

        self.window.buttonBack.setVisible(False)
        self.window.buttonForward.setVisible(False)
        self.window.buttonAddPatientInDB.setText('Изменить')
        self.window.tabWidget.setCurrentIndex(3)

    """
    # Удаление данных о пациенте
    """

    def removePatient(self):

        if self.window.tablePatient.currentRow() == -1:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Внимание")
            msgBox.setText("Выберите пациента")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.exec()
            return

        if self.controller.removePatient(self.window.tablePatient.item(self.window.tablePatient.currentRow(),1).text()):
            self.window.tablePatient.removeRow(self.window.tablePatient.currentRow())

    """
        # Анализ данных
    """
    def startAnalyze(self):

        try:
            a = sitk.ReadImage(self.window.labelFilePath.text())
            if a is None:
                raise Exception('Unable open CT-snapshot.')
        except Exception as e:
            logger.exception('Не удалось открыть КТ-снимок')
            self.writeAnalyzeInLog(f'Ошибка чтения файла: {self.window.labelFilePath.text()}')
            QMessageBox.critical(
              None,
              "Ошибка!",
              f"Не удалось открыть файл с КТ-снимком, загрузите файл!",
            )
            return
        self.writeAnalyzeInLog('Загрузка модели...')

        self.window.buttonStartAnalyze.setEnabled(False)
        self.window.progressAnalyze.setFormat('Load model...')
        self.window.progressAnalyze.setValue(33)

        self.controller.startAnalyze(self.window.labelFilePath.text())

    def writeAnalyzeInLog(self, string):

        date1 = '[' + datetime.today().strftime('%d-%m-%Y %H:%M:%S') + '] '
        self.window.plainTextEditAnalyze.setPlainText(
            "".join([
                self.window.plainTextEditAnalyze.toPlainText(),
                date1 + string
                ]) + '\n'
            )
    def changeProgressBar(self, item):
        item = item[0]

        data = {
            0 : 'Classify and discern...',
            1 : 'Completed',
            2 : 'Classification error!',
            3 : 'Loading error!',
            4 : 'Segmentify...'
        }

        logs = {
            0 : 'Классификация и распознавание данных...',
            1 : 'Работа нейросети окончена.',
            2 : 'Выявлены ошибки при классификации/распознавании. Подробнее: data.log',
            3 : 'Выявлены ошибки при загрузке модели. Подробнее: data.log',
            4 : 'Сегментация данных...',
            5 : 'Выявлены ошибки при сегментации. Подробнее: data.log',
        }

        if type(item) == int:
            self.window.progressAnalyze.setFormat(data[item])
            if item in [0,1,4]:
                self.window.progressAnalyze.setValue(self.window.progressAnalyze.value() + 25)
            else:
                self.window.progressAnalyze.setValue(0)
                self.window.buttonStartAnalyze.setEnabled(True)
            self.writeAnalyzeInLog(logs[item])
        elif type(item) == list:
            #self.window.textEditResult.setText('Lung cancer class: ' + item[0])
            item.append(self.window.labelFilePath.text())
            self.resultData = Result(item)
            self.canvas.draw_img(self.resultData)
            self.window.progressAnalyze.setValue(100)
            self.window.buttonStartAnalyze.setEnabled(True)
            self.window.tabWidget.setCurrentIndex(2)

    def getResultData(self):
        cur = self.window.tablePatient.currentRow()
        return [
            self.window.tablePatient.item(cur, 1).text(),
            self.resultData.imgClass,
            self.resultData.segmentatedImg,
            self.controller.image_to_byte_array(self.resultData.pathToInitImg)
        ]

    def dataIsSaved(self, isSaved):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Уведомление")
        if isSaved:
            msgBox.setText("Данные успешно сохранены.")
        else:
            msgBox.setText("Не удалось сохранить данные.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec()
    """
        # События устройств ввода
    """
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = QPoint()

    def mouseMoveEvent(self, event):
        if not self.__press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.__press_pos))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and self.window.tabWidget.currentIndex() == 0:
            self.window.tabWidget.setCurrentIndex(1)
        event.accept()

    """
        # etc
    """

    def closeEvent(self, event):
        if self.controller.mia.work:
            event.ignore()
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Внимание")
            msgBox.setText("Данные еще обрабатываются.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.exec()
        else:
            event.accept()
            

    def loadFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"Image files (*.jpg *.dcm *.png)")
        self.window.labelFilePath.setText(fname[0])

    def aboutProgram(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("О программе")
        #msgBox.setText("Система медицинской диагностики")
        msgBox.setText("Программа (бета-версия) предназначена для \
классификации злокачественных образований, наблюдающихся при раке легкого. \
Для удобства работы в программе реализован пользовательский интерфейс. \
В прилагающейся БД программа хранит данные для авторизации, данные о \
пациентах и результаты анализов. Пользователь загружает КT-снимок, \
соотнося его с информацией о пациенте. Классификатор обрабатывает снимок и выводит тип злокачественной опухоли.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setDefaultButton(QMessageBox.Ok)

        msgBox.exec()

