# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyMoneyOrgaGui.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyMoneyOrgaGui(object):
    def setupUi(self, PyMoneyOrgaGui):
        PyMoneyOrgaGui.setObjectName("PyMoneyOrgaGui")
        PyMoneyOrgaGui.resize(659, 488)
        self.centralwidget = QtWidgets.QWidget(PyMoneyOrgaGui)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tabOrganizeAccounts = QtWidgets.QWidget()
        self.tabOrganizeAccounts.setObjectName("tabOrganizeAccounts")
        self.widget = QtWidgets.QWidget(self.tabOrganizeAccounts)
        self.widget.setGeometry(QtCore.QRect(10, 10, 480, 251))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonAddExpenses = QtWidgets.QPushButton(self.widget)
        self.buttonAddExpenses.setObjectName("buttonAddExpenses")
        self.gridLayout.addWidget(self.buttonAddExpenses, 4, 0, 1, 1)
        self.labelAddExpenses = QtWidgets.QLabel(self.widget)
        self.labelAddExpenses.setObjectName("labelAddExpenses")
        self.gridLayout.addWidget(self.labelAddExpenses, 3, 1, 1, 1)
        self.comboChooseAccount = QtWidgets.QComboBox(self.widget)
        self.comboChooseAccount.setObjectName("comboChooseAccount")
        self.comboChooseAccount.addItem("")
        self.gridLayout.addWidget(self.comboChooseAccount, 2, 1, 1, 1)
        self.inputAddExpenses = QtWidgets.QLineEdit(self.widget)
        self.inputAddExpenses.setObjectName("inputAddExpenses")
        self.gridLayout.addWidget(self.inputAddExpenses, 4, 1, 1, 1)
        self.labelChooseAccount = QtWidgets.QLabel(self.widget)
        self.labelChooseAccount.setObjectName("labelChooseAccount")
        self.gridLayout.addWidget(self.labelChooseAccount, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.tableViewAccounts = QtWidgets.QTableView(self.widget)
        self.tableViewAccounts.setShowGrid(True)
        self.tableViewAccounts.setObjectName("tableViewAccounts")
        self.gridLayout.addWidget(self.tableViewAccounts, 0, 2, 6, 1)
        self.tabWidget.addTab(self.tabOrganizeAccounts, "")
        PyMoneyOrgaGui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyMoneyOrgaGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PyMoneyOrgaGui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyMoneyOrgaGui)
        self.statusbar.setObjectName("statusbar")
        PyMoneyOrgaGui.setStatusBar(self.statusbar)
        self.actionCreate_New_Account = QtWidgets.QAction(PyMoneyOrgaGui)
        self.actionCreate_New_Account.setObjectName("actionCreate_New_Account")
        self.menuFile.addAction(self.actionCreate_New_Account)
        self.menubar.addAction(self.menuFile.menuAction())
        self.labelAddExpenses.setBuddy(self.inputAddExpenses)
        self.labelChooseAccount.setBuddy(self.comboChooseAccount)

        self.retranslateUi(PyMoneyOrgaGui)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PyMoneyOrgaGui)

    def retranslateUi(self, PyMoneyOrgaGui):
        _translate = QtCore.QCoreApplication.translate
        PyMoneyOrgaGui.setWindowTitle(_translate("PyMoneyOrgaGui", "PyMoneyOrga"))
        self.buttonAddExpenses.setText(_translate("PyMoneyOrgaGui", "new expenses"))
        self.labelAddExpenses.setText(_translate("PyMoneyOrgaGui", "expenses"))
        self.comboChooseAccount.setItemText(0, _translate("PyMoneyOrgaGui", "NoAccountSaved"))
        self.labelChooseAccount.setText(_translate("PyMoneyOrgaGui", "choose account"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOrganizeAccounts), _translate("PyMoneyOrgaGui", "Organize Expenses"))
        self.menuFile.setTitle(_translate("PyMoneyOrgaGui", "File"))
        self.actionCreate_New_Account.setText(_translate("PyMoneyOrgaGui", "Create New Account"))

