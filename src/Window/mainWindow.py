# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 615)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("font: 10pt corbel;\n"
"background: rgb(245, 245, 245);    ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 120, 671, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("QTabWidget QWidget {\n"
"    background: rgb(245, 245, 245);\n"
"    color:black;\n"
"}\n"
"QTabWidget::pane {\n"
"  border: none;\n"
"} \n"
"\n"
"QTabBar::tab{\n"
"    background: red;\n"
"    width:0; \n"
"    height: 0;         \n"
"    margin: 0;\n"
"    padding: 0;\n"
"    border: none;\n"
"} \n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.startAnalyze = QtWidgets.QWidget()
        self.startAnalyze.setStyleSheet("")
        self.startAnalyze.setObjectName("startAnalyze")
        self.formLayout_3 = QtWidgets.QFormLayout(self.startAnalyze)
        self.formLayout_3.setObjectName("formLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditSearch = QtWidgets.QLineEdit(self.startAnalyze)
        self.lineEditSearch.setStyleSheet("background-color: white;")
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.horizontalLayout_2.addWidget(self.lineEditSearch)
        self.buttonSearch = QtWidgets.QPushButton(self.startAnalyze)
        self.buttonSearch.setObjectName("buttonSearch")
        self.horizontalLayout_2.addWidget(self.buttonSearch)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.tablePatient = QtWidgets.QTableWidget(self.startAnalyze)
        self.tablePatient.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablePatient.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablePatient.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablePatient.setObjectName("tablePatient")
        self.tablePatient.setColumnCount(0)
        self.tablePatient.setRowCount(0)
        self.tablePatient.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_6.addWidget(self.tablePatient)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonDownFile = QtWidgets.QPushButton(self.startAnalyze)
        self.buttonDownFile.setObjectName("buttonDownFile")
        self.gridLayout.addWidget(self.buttonDownFile, 1, 0, 1, 1)
        self.buttonAddPatient = QtWidgets.QPushButton(self.startAnalyze)
        self.buttonAddPatient.setObjectName("buttonAddPatient")
        self.gridLayout.addWidget(self.buttonAddPatient, 0, 0, 1, 1)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(16)
        self.formLayout.setObjectName("formLayout")
        self.labelSurname_2 = QtWidgets.QLabel(self.startAnalyze)
        self.labelSurname_2.setObjectName("labelSurname_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSurname_2)
        self.surnamePatient = QtWidgets.QLabel(self.startAnalyze)
        self.surnamePatient.setStyleSheet("background-color: white;")
        self.surnamePatient.setText("")
        self.surnamePatient.setObjectName("surnamePatient")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.surnamePatient)
        self.labelName_2 = QtWidgets.QLabel(self.startAnalyze)
        self.labelName_2.setObjectName("labelName_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName_2)
        self.namePatient = QtWidgets.QLabel(self.startAnalyze)
        self.namePatient.setStyleSheet("background-color: white;")
        self.namePatient.setText("")
        self.namePatient.setObjectName("namePatient")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.namePatient)
        self.labelPatronymic_2 = QtWidgets.QLabel(self.startAnalyze)
        self.labelPatronymic_2.setObjectName("labelPatronymic_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelPatronymic_2)
        self.patronymicPatient = QtWidgets.QLabel(self.startAnalyze)
        self.patronymicPatient.setStyleSheet("background-color: white;")
        self.patronymicPatient.setText("")
        self.patronymicPatient.setObjectName("patronymicPatient")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.patronymicPatient)
        self.labelDate = QtWidgets.QLabel(self.startAnalyze)
        self.labelDate.setObjectName("labelDate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelDate)
        self.datePatient = QtWidgets.QLabel(self.startAnalyze)
        self.datePatient.setStyleSheet("background-color: white;")
        self.datePatient.setText("")
        self.datePatient.setObjectName("datePatient")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.datePatient)
        self.labelGender = QtWidgets.QLabel(self.startAnalyze)
        self.labelGender.setObjectName("labelGender")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelGender)
        self.genderPatient = QtWidgets.QLabel(self.startAnalyze)
        self.genderPatient.setStyleSheet("background-color: white;")
        self.genderPatient.setText("")
        self.genderPatient.setObjectName("genderPatient")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.genderPatient)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        self.tabWidget.addTab(self.startAnalyze, "")
        self.downloadFile = QtWidgets.QWidget()
        self.downloadFile.setObjectName("downloadFile")
        self.formLayout_4 = QtWidgets.QFormLayout(self.downloadFile)
        self.formLayout_4.setObjectName("formLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_4.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelFilePath = QtWidgets.QLabel(self.downloadFile)
        self.labelFilePath.setText("")
        self.labelFilePath.setObjectName("labelFilePath")
        self.verticalLayout_7.addWidget(self.labelFilePath)
        self.buttonLoadFile = QtWidgets.QPushButton(self.downloadFile)
        self.buttonLoadFile.setStyleSheet("")
        self.buttonLoadFile.setObjectName("buttonLoadFile")
        self.verticalLayout_7.addWidget(self.buttonLoadFile)
        self.buttonAnalyze = QtWidgets.QPushButton(self.downloadFile)
        self.buttonAnalyze.setObjectName("buttonAnalyze")
        self.verticalLayout_7.addWidget(self.buttonAnalyze)
        self.index1ButtonBack = QtWidgets.QPushButton(self.downloadFile)
        self.index1ButtonBack.setObjectName("index1ButtonBack")
        self.verticalLayout_7.addWidget(self.index1ButtonBack)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout_7)
        self.tabWidget.addTab(self.downloadFile, "")
        self.Analyze = QtWidgets.QWidget()
        self.Analyze.setObjectName("Analyze")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Analyze)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 60, 641, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressAnalyze = QtWidgets.QProgressBar(self.verticalLayoutWidget_3)
        self.progressAnalyze.setProperty("value", 0)
        self.progressAnalyze.setObjectName("progressAnalyze")
        self.verticalLayout_4.addWidget(self.progressAnalyze)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.Analyze)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(500, 390, 160, 80))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.buttonResult = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.buttonResult.setObjectName("buttonResult")
        self.verticalLayout_8.addWidget(self.buttonResult)
        self.index2ButtonBack = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.index2ButtonBack.setObjectName("index2ButtonBack")
        self.verticalLayout_8.addWidget(self.index2ButtonBack)
        self.buttonStartAnalyze = QtWidgets.QPushButton(self.Analyze)
        self.buttonStartAnalyze.setGeometry(QtCore.QRect(20, 110, 131, 25))
        self.buttonStartAnalyze.setStyleSheet("")
        self.buttonStartAnalyze.setObjectName("buttonStartAnalyze")
        self.tabWidget.addTab(self.Analyze, "")
        self.resultAnalyze = QtWidgets.QWidget()
        self.resultAnalyze.setObjectName("resultAnalyze")
        self.textEditResult = QtWidgets.QTextEdit(self.resultAnalyze)
        self.textEditResult.setGeometry(QtCore.QRect(30, 50, 391, 331))
        self.textEditResult.setStyleSheet("background: white")
        self.textEditResult.setObjectName("textEditResult")
        self.label = QtWidgets.QLabel(self.resultAnalyze)
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 21))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.resultAnalyze)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(500, 390, 160, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.saveDB = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.saveDB.setStyleSheet("")
        self.saveDB.setObjectName("saveDB")
        self.verticalLayout_5.addWidget(self.saveDB)
        self.index3ButtonBack = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.index3ButtonBack.setObjectName("index3ButtonBack")
        self.verticalLayout_5.addWidget(self.index3ButtonBack)
        self.tabWidget.addTab(self.resultAnalyze, "")
        self.addPatient = QtWidgets.QWidget()
        self.addPatient.setObjectName("addPatient")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.addPatient)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 50, 581, 231))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelSurname = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelSurname.setObjectName("labelSurname")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSurname)
        self.lineEditSurname = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditSurname)
        self.labelName = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelName.setObjectName("labelName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEditName.setText("")
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.labelPatronymic = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelPatronymic.setObjectName("labelPatronymic")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelPatronymic)
        self.lineEditPatronymic = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEditPatronymic.setObjectName("lineEditPatronymic")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditPatronymic)
        self.labelBirthDate = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelBirthDate.setObjectName("labelBirthDate")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelBirthDate)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonAddPatientInDB = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.buttonAddPatientInDB.setObjectName("buttonAddPatientInDB")
        self.verticalLayout_2.addWidget(self.buttonAddPatientInDB)
        self.index4ButtonBack = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.index4ButtonBack.setObjectName("index4ButtonBack")
        self.verticalLayout_2.addWidget(self.index4ButtonBack)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.tabWidget.addTab(self.addPatient, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(410, 50, 281, 61))
        self.groupBox.setMinimumSize(QtCore.QSize(281, 61))
        self.groupBox.setMaximumSize(QtCore.QSize(281, 61))
        self.groupBox.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.groupBox.setObjectName("groupBox")
        self.buttonExit = QtWidgets.QPushButton(self.groupBox)
        self.buttonExit.setGeometry(QtCore.QRect(180, 20, 93, 28))
        self.buttonExit.setStyleSheet("")
        self.buttonExit.setObjectName("buttonExit")
        self.User = QtWidgets.QLabel(self.groupBox)
        self.User.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.User.setStyleSheet("background-color:white")
        self.User.setObjectName("User")
        self.tabBar = QtWidgets.QGroupBox(self.centralwidget)
        self.tabBar.setGeometry(QtCore.QRect(0, 0, 701, 40))
        self.tabBar.setStyleSheet("background-color: black; font: 10pt")
        self.tabBar.setTitle("")
        self.tabBar.setObjectName("tabBar")
        self.buttonClose = QtWidgets.QPushButton(self.tabBar)
        self.buttonClose.setGeometry(QtCore.QRect(660, 5, 31, 31))
        self.buttonClose.setStyleSheet("color: white")
        self.buttonClose.setText("")
        self.buttonClose.setObjectName("buttonClose")
        self.buttonInfo = QtWidgets.QPushButton(self.tabBar)
        self.buttonInfo.setGeometry(QtCore.QRect(620, 5, 31, 31))
        self.buttonInfo.setStyleSheet("color: white")
        self.buttonInfo.setText("")
        self.buttonInfo.setObjectName("buttonInfo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система меддиагностики"))
        self.buttonSearch.setText(_translate("MainWindow", "Поиск"))
        self.buttonDownFile.setText(_translate("MainWindow", "Далее"))
        self.buttonAddPatient.setText(_translate("MainWindow", "Добавить пациента"))
        self.labelSurname_2.setText(_translate("MainWindow", "Фамилия"))
        self.labelName_2.setText(_translate("MainWindow", "Имя"))
        self.labelPatronymic_2.setText(_translate("MainWindow", "Отчество"))
        self.labelDate.setText(_translate("MainWindow", "Дата рождения"))
        self.labelGender.setText(_translate("MainWindow", "Пол"))
        self.buttonLoadFile.setText(_translate("MainWindow", "Загрузить файл"))
        self.buttonAnalyze.setText(_translate("MainWindow", "Далее"))
        self.index1ButtonBack.setText(_translate("MainWindow", "назад"))
        self.progressAnalyze.setFormat(_translate("MainWindow", "Waiting..."))
        self.buttonResult.setText(_translate("MainWindow", "Далее"))
        self.index2ButtonBack.setText(_translate("MainWindow", "Назад"))
        self.buttonStartAnalyze.setText(_translate("MainWindow", "Анализ"))
        self.label.setText(_translate("MainWindow", "Результаты анализа"))
        self.saveDB.setText(_translate("MainWindow", "Cохранить в бд"))
        self.index3ButtonBack.setText(_translate("MainWindow", "назад"))
        self.labelSurname.setText(_translate("MainWindow", "Фамилия"))
        self.labelName.setText(_translate("MainWindow", "Имя"))
        self.labelPatronymic.setText(_translate("MainWindow", "Отчество"))
        self.labelBirthDate.setText(_translate("MainWindow", "Дата рождения"))
        self.buttonAddPatientInDB.setText(_translate("MainWindow", "Добавить"))
        self.index4ButtonBack.setText(_translate("MainWindow", "назад"))
        self.groupBox.setTitle(_translate("MainWindow", "Пользователь"))
        self.buttonExit.setText(_translate("MainWindow", "выход"))
        self.User.setText(_translate("MainWindow", "Авдеев И.А"))
