# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyMoneyOrgaGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyMoneyOrgaGui(object):
    def setupUi(self, PyMoneyOrgaGui):
        PyMoneyOrgaGui.setObjectName("PyMoneyOrgaGui")
        PyMoneyOrgaGui.resize(1218, 725)
        PyMoneyOrgaGui.setMinimumSize(QtCore.QSize(0, 0))
        PyMoneyOrgaGui.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(PyMoneyOrgaGui)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 7, 1, 1, 1)
        self.comboChooseAccount = QtWidgets.QComboBox(self.centralwidget)
        self.comboChooseAccount.setObjectName("comboChooseAccount")
        self.comboChooseAccount.addItem("")
        self.gridLayout_2.addWidget(self.comboChooseAccount, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 8, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.inputAddExpenses = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAddExpenses.setObjectName("inputAddExpenses")
        self.gridLayout_4.addWidget(self.inputAddExpenses, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 1, 1, 1)
        self.buttonAddIncome = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddIncome.setObjectName("buttonAddIncome")
        self.gridLayout_2.addWidget(self.buttonAddIncome, 3, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 1, 1, 1)
        self.labelAddExpenses = QtWidgets.QLabel(self.centralwidget)
        self.labelAddExpenses.setObjectName("labelAddExpenses")
        self.gridLayout_7.addWidget(self.labelAddExpenses, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_7, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        self.buttonAddExpenses = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddExpenses.setObjectName("buttonAddExpenses")
        self.gridLayout_2.addWidget(self.buttonAddExpenses, 2, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 6, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.inputAddIncome = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAddIncome.setObjectName("inputAddIncome")
        self.gridLayout_6.addWidget(self.inputAddIncome, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 3, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 9, 1, 1, 1)
        self.labelChooseAccount = QtWidgets.QLabel(self.centralwidget)
        self.labelChooseAccount.setObjectName("labelChooseAccount")
        self.gridLayout_2.addWidget(self.labelChooseAccount, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetTransactions = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetTransactions.setObjectName("tableWidgetTransactions")
        self.tableWidgetTransactions.setColumnCount(3)
        self.tableWidgetTransactions.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetTransactions.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetTransactions.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetTransactions.setHorizontalHeaderItem(2, item)
        self.tableWidgetTransactions.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetTransactions.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidgetTransactions.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetTransactions.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetTransactions.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidgetTransactions, 0, 2, 3, 1)
        self.tableWidgetAccounts = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetAccounts.setShowGrid(True)
        self.tableWidgetAccounts.setObjectName("tableWidgetAccounts")
        self.tableWidgetAccounts.setColumnCount(2)
        self.tableWidgetAccounts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAccounts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAccounts.setHorizontalHeaderItem(1, item)
        self.tableWidgetAccounts.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetAccounts.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidgetAccounts.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetAccounts.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidgetAccounts, 0, 1, 3, 1)
        spacerItem2 = QtWidgets.QSpacerItem(450, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(350, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.gridLayout_9.addWidget(self.tabWidget_2, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        PyMoneyOrgaGui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyMoneyOrgaGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1218, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PyMoneyOrgaGui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyMoneyOrgaGui)
        self.statusbar.setObjectName("statusbar")
        PyMoneyOrgaGui.setStatusBar(self.statusbar)
        self.actionCreate_New_Account = QtWidgets.QAction(PyMoneyOrgaGui)
        self.actionCreate_New_Account.setObjectName("actionCreate_New_Account")
        self.actionDeleteAccount = QtWidgets.QAction(PyMoneyOrgaGui)
        self.actionDeleteAccount.setObjectName("actionDeleteAccount")
        self.actionDelete_Account = QtWidgets.QAction(PyMoneyOrgaGui)
        self.actionDelete_Account.setObjectName("actionDelete_Account")
        self.actionExit = QtWidgets.QAction(PyMoneyOrgaGui)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionCreate_New_Account)
        self.menuFile.addAction(self.actionDeleteAccount)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.labelAddExpenses.setBuddy(self.inputAddExpenses)
        self.labelChooseAccount.setBuddy(self.comboChooseAccount)

        self.retranslateUi(PyMoneyOrgaGui)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PyMoneyOrgaGui)
        PyMoneyOrgaGui.setTabOrder(self.tableWidgetAccounts, self.tableWidgetTransactions)

    def retranslateUi(self, PyMoneyOrgaGui):
        _translate = QtCore.QCoreApplication.translate
        PyMoneyOrgaGui.setWindowTitle(_translate("PyMoneyOrgaGui", "PyMoneyOrga"))
        self.checkBox_3.setText(_translate("PyMoneyOrgaGui", "Amount"))
        self.comboChooseAccount.setItemText(0, _translate("PyMoneyOrgaGui", "NoAccountSaved"))
        self.checkBox.setText(_translate("PyMoneyOrgaGui", "New balance"))
        self.label.setText(_translate("PyMoneyOrgaGui", "What to show in transaction table"))
        self.buttonAddIncome.setText(_translate("PyMoneyOrgaGui", "New income"))
        self.label_2.setText(_translate("PyMoneyOrgaGui", "Description"))
        self.labelAddExpenses.setText(_translate("PyMoneyOrgaGui", "Amount"))
        self.buttonAddExpenses.setText(_translate("PyMoneyOrgaGui", "New expenses"))
        self.checkBox_2.setText(_translate("PyMoneyOrgaGui", "Time stamp"))
        self.checkBox_4.setText(_translate("PyMoneyOrgaGui", "Description"))
        self.labelChooseAccount.setText(_translate("PyMoneyOrgaGui", "Choose account"))
        self.tableWidgetTransactions.setSortingEnabled(True)
        item = self.tableWidgetTransactions.horizontalHeaderItem(0)
        item.setText(_translate("PyMoneyOrgaGui", "Time stamp"))
        item = self.tableWidgetTransactions.horizontalHeaderItem(1)
        item.setText(_translate("PyMoneyOrgaGui", "Amount"))
        item = self.tableWidgetTransactions.horizontalHeaderItem(2)
        item.setText(_translate("PyMoneyOrgaGui", "New balance"))
        self.tableWidgetAccounts.setSortingEnabled(True)
        item = self.tableWidgetAccounts.horizontalHeaderItem(0)
        item.setText(_translate("PyMoneyOrgaGui", "Account"))
        item = self.tableWidgetAccounts.horizontalHeaderItem(1)
        item.setText(_translate("PyMoneyOrgaGui", "Balance"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("PyMoneyOrgaGui", "Table view"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("PyMoneyOrgaGui", "Graphical view"))
        self.menuFile.setTitle(_translate("PyMoneyOrgaGui", "File"))
        self.actionCreate_New_Account.setText(_translate("PyMoneyOrgaGui", "Create New Account"))
        self.actionDeleteAccount.setText(_translate("PyMoneyOrgaGui", "Delete Account"))
        self.actionDelete_Account.setText(_translate("PyMoneyOrgaGui", "Delete Account"))
        self.actionExit.setText(_translate("PyMoneyOrgaGui", "Exit"))
