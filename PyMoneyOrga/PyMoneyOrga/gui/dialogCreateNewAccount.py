# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogCreateNewAccount.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogCreateNewAccount(object):
    def setupUi(self, dialogCreateNewAccount):
        dialogCreateNewAccount.setObjectName("dialogCreateNewAccount")
        dialogCreateNewAccount.resize(478, 336)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialogCreateNewAccount)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.inputAccountName = QtWidgets.QLineEdit(dialogCreateNewAccount)
        self.inputAccountName.setGeometry(QtCore.QRect(250, 113, 200, 20))
        self.inputAccountName.setObjectName("inputAccountName")
        self.labelAccountName = QtWidgets.QLabel(dialogCreateNewAccount)
        self.labelAccountName.setGeometry(QtCore.QRect(250, 72, 200, 35))
        self.labelAccountName.setObjectName("labelAccountName")
        self.inputInitialAmount = QtWidgets.QLineEdit(dialogCreateNewAccount)
        self.inputInitialAmount.setGeometry(QtCore.QRect(250, 180, 200, 20))
        self.inputInitialAmount.setObjectName("inputInitialAmount")
        self.labelFirstAmount = QtWidgets.QLabel(dialogCreateNewAccount)
        self.labelFirstAmount.setGeometry(QtCore.QRect(250, 139, 200, 34))
        self.labelFirstAmount.setObjectName("labelFirstAmount")
        self.buttonAddNewAccount = QtWidgets.QPushButton(dialogCreateNewAccount)
        self.buttonAddNewAccount.setGeometry(QtCore.QRect(44, 179, 200, 23))
        self.buttonAddNewAccount.setObjectName("buttonAddNewAccount")
        self.labelAccountName.setBuddy(self.inputAccountName)
        self.labelFirstAmount.setBuddy(self.inputInitialAmount)

        self.retranslateUi(dialogCreateNewAccount)
        self.buttonBox.clicked['QAbstractButton*'].connect(dialogCreateNewAccount.close)
        QtCore.QMetaObject.connectSlotsByName(dialogCreateNewAccount)

    def retranslateUi(self, dialogCreateNewAccount):
        _translate = QtCore.QCoreApplication.translate
        dialogCreateNewAccount.setWindowTitle(_translate("dialogCreateNewAccount", "Create New Account"))
        self.labelAccountName.setText(_translate("dialogCreateNewAccount", "Account name"))
        self.labelFirstAmount.setText(_translate("dialogCreateNewAccount", "Starting amount of money"))
        self.buttonAddNewAccount.setText(_translate("dialogCreateNewAccount", "Add new account"))
