# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/authorizationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_authorization(object):
    def setupUi(self, authorization):
        authorization.setObjectName("authorization")
        authorization.setWindowModality(QtCore.Qt.ApplicationModal)
        authorization.resize(410, 300)
        authorization.setMinimumSize(QtCore.QSize(410, 300))
        authorization.setMaximumSize(QtCore.QSize(410, 300))
        authorization.setAutoFillBackground(False)
        authorization.setStyleSheet("background-color:rgb(211, 211, 211)")
        self.userName = QtWidgets.QLineEdit(authorization)
        self.userName.setGeometry(QtCore.QRect(120, 130, 161, 22))
        self.userName.setStyleSheet("background-color: white")
        self.userName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userName.setObjectName("userName")
        self.label_3 = QtWidgets.QLabel(authorization)
        self.label_3.setGeometry(QtCore.QRect(90, 50, 221, 51))
        self.label_3.setStyleSheet("font: 16pt corbel;\n"
"color: black")
        self.label_3.setObjectName("label_3")
        self.userPassword = QtWidgets.QLineEdit(authorization)
        self.userPassword.setGeometry(QtCore.QRect(120, 170, 161, 22))
        self.userPassword.setStyleSheet("background-color: white")
        self.userPassword.setText("")
        self.userPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userPassword.setObjectName("userPassword")
        self.buttonEntrance = QtWidgets.QPushButton(authorization)
        self.buttonEntrance.setGeometry(QtCore.QRect(270, 240, 93, 28))
        self.buttonEntrance.setStyleSheet("")
        self.buttonEntrance.setObjectName("buttonEntrance")
        self.label = QtWidgets.QLabel(authorization)
        self.label.setGeometry(QtCore.QRect(80, 120, 31, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/img/user.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(authorization)
        self.label_2.setGeometry(QtCore.QRect(80, 170, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ui/img/key.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(authorization)
        QtCore.QMetaObject.connectSlotsByName(authorization)

    def retranslateUi(self, authorization):
        _translate = QtCore.QCoreApplication.translate
        authorization.setWindowTitle(_translate("authorization", "Авторизация"))
        self.label_3.setText(_translate("authorization", "Добро пожаловать"))
        self.buttonEntrance.setText(_translate("authorization", "Вход"))
