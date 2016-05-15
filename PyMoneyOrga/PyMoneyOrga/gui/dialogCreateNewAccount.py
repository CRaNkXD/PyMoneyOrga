# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogCreateNewAccount.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogCreateNewAccount(object):
    def setupUi(self, dialogCreateNewAccount):
        dialogCreateNewAccount.setObjectName("dialogCreateNewAccount")
        dialogCreateNewAccount.setEnabled(True)
        dialogCreateNewAccount.resize(404, 172)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogCreateNewAccount.sizePolicy().hasHeightForWidth())
        dialogCreateNewAccount.setSizePolicy(sizePolicy)
        dialogCreateNewAccount.setMinimumSize(QtCore.QSize(400, 170))
        dialogCreateNewAccount.setSizeGripEnabled(False)
        dialogCreateNewAccount.setModal(False)
        self.widget = QtWidgets.QWidget(dialogCreateNewAccount)
        self.widget.setGeometry(QtCore.QRect(20, 20, 361, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.labelAccountName = QtWidgets.QLabel(self.widget)
        self.labelAccountName.setObjectName("labelAccountName")
        self.gridLayout.addWidget(self.labelAccountName, 0, 1, 1, 1)
        self.inputAccountName = QtWidgets.QLineEdit(self.widget)
        self.inputAccountName.setObjectName("inputAccountName")
        self.gridLayout.addWidget(self.inputAccountName, 1, 1, 1, 1)
        self.labelFirstAmount = QtWidgets.QLabel(self.widget)
        self.labelFirstAmount.setObjectName("labelFirstAmount")
        self.gridLayout.addWidget(self.labelFirstAmount, 2, 1, 1, 1)
        self.buttonAddNewAccount = QtWidgets.QPushButton(self.widget)
        self.buttonAddNewAccount.setObjectName("buttonAddNewAccount")
        self.gridLayout.addWidget(self.buttonAddNewAccount, 3, 0, 1, 1)
        self.inputInitialAmount = QtWidgets.QLineEdit(self.widget)
        self.inputInitialAmount.setObjectName("inputInitialAmount")
        self.gridLayout.addWidget(self.inputInitialAmount, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.buttonBox.raise_()
        self.labelAccountName.raise_()
        self.buttonAddNewAccount.raise_()
        self.inputAccountName.raise_()
        self.inputInitialAmount.raise_()
        self.labelFirstAmount.raise_()
        self.buttonBox.raise_()
        self.buttonBox.raise_()
        self.buttonBox.raise_()
        self.buttonAddNewAccount.raise_()
        self.inputAccountName.raise_()
        self.labelAccountName.raise_()
        self.inputInitialAmount.raise_()
        self.labelFirstAmount.raise_()
        self.labelAccountName.setBuddy(self.inputAccountName)
        self.labelFirstAmount.setBuddy(self.inputInitialAmount)

        self.retranslateUi(dialogCreateNewAccount)
        self.buttonBox.accepted.connect(dialogCreateNewAccount.accept)
        self.buttonBox.rejected.connect(dialogCreateNewAccount.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogCreateNewAccount)

    def retranslateUi(self, dialogCreateNewAccount):
        _translate = QtCore.QCoreApplication.translate
        dialogCreateNewAccount.setWindowTitle(_translate("dialogCreateNewAccount", "CreateNewAccount"))
        self.labelAccountName.setText(_translate("dialogCreateNewAccount", "Account name"))
        self.labelFirstAmount.setText(_translate("dialogCreateNewAccount", "Starting amount of money"))
        self.buttonAddNewAccount.setText(_translate("dialogCreateNewAccount", "Add new account"))

