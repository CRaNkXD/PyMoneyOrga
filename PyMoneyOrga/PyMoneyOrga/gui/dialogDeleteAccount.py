# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogDeleteAccount.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogDeleteAccount(object):
    def setupUi(self, dialogDeleteAccount):
        dialogDeleteAccount.setObjectName("dialogDeleteAccount")
        dialogDeleteAccount.resize(486, 148)
        self.gridLayout_2 = QtWidgets.QGridLayout(dialogDeleteAccount)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboChooseAccount = QtWidgets.QComboBox(dialogDeleteAccount)
        self.comboChooseAccount.setObjectName("comboChooseAccount")
        self.comboChooseAccount.addItem("")
        self.gridLayout.addWidget(self.comboChooseAccount, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttonDeleteAccount = QtWidgets.QPushButton(dialogDeleteAccount)
        self.buttonDeleteAccount.setObjectName("buttonDeleteAccount")
        self.gridLayout_4.addWidget(self.buttonDeleteAccount, 1, 1, 1, 1)
        self.buttonCancel = QtWidgets.QPushButton(dialogDeleteAccount)
        self.buttonCancel.setObjectName("buttonCancel")
        self.gridLayout_4.addWidget(self.buttonCancel, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(dialogDeleteAccount)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(dialogDeleteAccount)
        QtCore.QMetaObject.connectSlotsByName(dialogDeleteAccount)

    def retranslateUi(self, dialogDeleteAccount):
        _translate = QtCore.QCoreApplication.translate
        dialogDeleteAccount.setWindowTitle(_translate("dialogDeleteAccount", "Delete Account"))
        self.comboChooseAccount.setItemText(0, _translate("dialogDeleteAccount", "NoAccountSaved"))
        self.buttonDeleteAccount.setText(_translate("dialogDeleteAccount", "Delete"))
        self.buttonCancel.setText(_translate("dialogDeleteAccount", "Cancel"))
        self.label.setText(_translate("dialogDeleteAccount", "Choose an account to delete"))
