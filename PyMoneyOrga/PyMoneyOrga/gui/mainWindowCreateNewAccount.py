# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowCreateNewAccount.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowCreateAccount(object):
    def setupUi(self, MainWindowCreateAccount):
        MainWindowCreateAccount.setObjectName("MainWindowCreateAccount")
        MainWindowCreateAccount.resize(434, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindowCreateAccount)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 361, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.labelAccountName = QtWidgets.QLabel(self.layoutWidget)
        self.labelAccountName.setObjectName("labelAccountName")
        self.gridLayout.addWidget(self.labelAccountName, 0, 1, 1, 1)
        self.inputAccountName = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputAccountName.setObjectName("inputAccountName")
        self.gridLayout.addWidget(self.inputAccountName, 1, 1, 1, 1)
        self.labelFirstAmount = QtWidgets.QLabel(self.layoutWidget)
        self.labelFirstAmount.setObjectName("labelFirstAmount")
        self.gridLayout.addWidget(self.labelFirstAmount, 2, 1, 1, 1)
        self.buttonAddNewAccount = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonAddNewAccount.setObjectName("buttonAddNewAccount")
        self.gridLayout.addWidget(self.buttonAddNewAccount, 3, 0, 1, 1)
        self.inputInitialAmount = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputInitialAmount.setObjectName("inputInitialAmount")
        self.gridLayout.addWidget(self.inputInitialAmount, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        MainWindowCreateAccount.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowCreateAccount)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        MainWindowCreateAccount.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowCreateAccount)
        self.statusbar.setObjectName("statusbar")
        MainWindowCreateAccount.setStatusBar(self.statusbar)
        self.labelAccountName.setBuddy(self.inputAccountName)
        self.labelFirstAmount.setBuddy(self.inputInitialAmount)

        self.retranslateUi(MainWindowCreateAccount)
        QtCore.QMetaObject.connectSlotsByName(MainWindowCreateAccount)

    def retranslateUi(self, MainWindowCreateAccount):
        _translate = QtCore.QCoreApplication.translate
        MainWindowCreateAccount.setWindowTitle(_translate("MainWindowCreateAccount", "MainWindow"))
        self.labelAccountName.setText(_translate("MainWindowCreateAccount", "Account name"))
        self.labelFirstAmount.setText(_translate("MainWindowCreateAccount", "Starting amount of money"))
        self.buttonAddNewAccount.setText(_translate("MainWindowCreateAccount", "Add new account"))

