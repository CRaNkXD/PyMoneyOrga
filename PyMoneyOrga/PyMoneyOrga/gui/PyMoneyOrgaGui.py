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
        PyMoneyOrgaGui.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PyMoneyOrgaGui)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tabOrganizeAccounts = QtWidgets.QWidget()
        self.tabOrganizeAccounts.setObjectName("tabOrganizeAccounts")
        self.buttonAddExpenses = QtWidgets.QPushButton(self.tabOrganizeAccounts)
        self.buttonAddExpenses.setGeometry(QtCore.QRect(20, 70, 91, 23))
        self.buttonAddExpenses.setObjectName("buttonAddExpenses")
        self.inputAddExpenses = QtWidgets.QLineEdit(self.tabOrganizeAccounts)
        self.inputAddExpenses.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.inputAddExpenses.setObjectName("inputAddExpenses")
        self.labelAddExpenses = QtWidgets.QLabel(self.tabOrganizeAccounts)
        self.labelAddExpenses.setGeometry(QtCore.QRect(120, 50, 51, 16))
        self.labelAddExpenses.setObjectName("labelAddExpenses")
        self.comboChooseAccount = QtWidgets.QComboBox(self.tabOrganizeAccounts)
        self.comboChooseAccount.setGeometry(QtCore.QRect(120, 20, 69, 22))
        self.comboChooseAccount.setObjectName("comboChooseAccount")
        self.comboChooseAccount.addItem("")
        self.labelChooseAccount = QtWidgets.QLabel(self.tabOrganizeAccounts)
        self.labelChooseAccount.setGeometry(QtCore.QRect(120, 0, 81, 16))
        self.labelChooseAccount.setObjectName("labelChooseAccount")
        self.tableViewAccounts = QtWidgets.QTableView(self.tabOrganizeAccounts)
        self.tableViewAccounts.setGeometry(QtCore.QRect(520, 10, 256, 192))
        self.tableViewAccounts.setShowGrid(True)
        self.tableViewAccounts.setObjectName("tableViewAccounts")
        self.tabWidget.addTab(self.tabOrganizeAccounts, "")
        PyMoneyOrgaGui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyMoneyOrgaGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyMoneyOrgaGui = QtWidgets.QMainWindow()
    ui = Ui_PyMoneyOrgaGui()
    ui.setupUi(PyMoneyOrgaGui)
    PyMoneyOrgaGui.show()
    sys.exit(app.exec_())

