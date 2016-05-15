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
        dialogCreateNewAccount.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialogCreateNewAccount)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelAccountName = QtWidgets.QLabel(dialogCreateNewAccount)
        self.labelAccountName.setGeometry(QtCore.QRect(170, 40, 101, 20))
        self.labelAccountName.setObjectName("labelAccountName")
        self.buttonAddNewAccount = QtWidgets.QPushButton(dialogCreateNewAccount)
        self.buttonAddNewAccount.setGeometry(QtCore.QRect(40, 100, 111, 23))
        self.buttonAddNewAccount.setObjectName("buttonAddNewAccount")
        self.inputAccountName = QtWidgets.QLineEdit(dialogCreateNewAccount)
        self.inputAccountName.setGeometry(QtCore.QRect(170, 60, 113, 20))
        self.inputAccountName.setObjectName("inputAccountName")
        self.inputInitialAmount = QtWidgets.QLineEdit(dialogCreateNewAccount)
        self.inputInitialAmount.setGeometry(QtCore.QRect(170, 100, 113, 20))
        self.inputInitialAmount.setObjectName("inputInitialAmount")
        self.labelFirstAmount = QtWidgets.QLabel(dialogCreateNewAccount)
        self.labelFirstAmount.setGeometry(QtCore.QRect(170, 80, 131, 20))
        self.labelFirstAmount.setObjectName("labelFirstAmount")
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
        self.buttonAddNewAccount.setText(_translate("dialogCreateNewAccount", "Add new account"))
        self.labelFirstAmount.setText(_translate("dialogCreateNewAccount", "Starting amount of money"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogCreateNewAccount = QtWidgets.QDialog()
    ui = Ui_dialogCreateNewAccount()
    ui.setupUi(dialogCreateNewAccount)
    dialogCreateNewAccount.show()
    sys.exit(app.exec_())

