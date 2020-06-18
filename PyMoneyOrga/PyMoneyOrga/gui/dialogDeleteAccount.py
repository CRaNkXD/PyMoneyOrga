# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogDeleteAccount.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogDeleteAccount(object):
    def setupUi(self, DialogDeleteAccount):
        DialogDeleteAccount.setObjectName("DialogDeleteAccount")
        DialogDeleteAccount.resize(486, 148)
        self.gridLayout_2 = QtWidgets.QGridLayout(DialogDeleteAccount)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(DialogDeleteAccount)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonDelete = QtWidgets.QPushButton(DialogDeleteAccount)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.gridLayout_4.addWidget(self.pushButtonDelete, 1, 1, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogDeleteAccount)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout_4.addWidget(self.pushButtonCancel, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(DialogDeleteAccount)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(DialogDeleteAccount)
        QtCore.QMetaObject.connectSlotsByName(DialogDeleteAccount)

    def retranslateUi(self, DialogDeleteAccount):
        _translate = QtCore.QCoreApplication.translate
        DialogDeleteAccount.setWindowTitle(_translate("DialogDeleteAccount", "Delete Account"))
        self.pushButtonDelete.setText(_translate("DialogDeleteAccount", "Delete"))
        self.pushButtonCancel.setText(_translate("DialogDeleteAccount", "Cancel"))
        self.label.setText(_translate("DialogDeleteAccount", "Choose an account to delete"))
