import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from .gui.PyMoneyOrgaGui import Ui_PyMoneyOrgaGui
from .gui.dialogCreateNewAccount import Ui_dialogCreateNewAccount
from .account import Account
from .database import Database


class DialogCreatNewAccount(QtWidgets.QDialog, Ui_dialogCreateNewAccount):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Connect add button with a custom function (addAcc)
        self.buttonAddNewAccount.clicked.connect(self.addAcc)

    def closeEvent(self, event):
        self.parent().dialogCreateNewAccount = None

    def addAcc(self):
        sAccName = str(self.inputAccountName.text())
        iCash = int(self.inputInitialAmount.text())
        cNewAcc = Account(sAccName, iCash)
        self.parent().cDatabase.addAcc(cNewAcc)
        itemAccName = QtGui.QStandardItem(sAccName)
        itemAccName.setEditable(False)
        itemCash = QtGui.QStandardItem(str(iCash))
        itemCash.setEditable(False)
        row = [itemAccName,itemCash]
        self.parent().modelTableViewAccounts.appendRow(row)
        for account in self.parent().cDatabase.acAllAccs:
            print(self.parent().cDatabase.acAllAccs[account].sAccName + '; ' + str(self.parent().cDatabase.acAllAccs[account].iCash))
        
        # delete the initial combo box item and add a new one for the account 
        if self.parent().comboChooseAccount.currentText() == "NoAccountSaved":
            self.parent().comboChooseAccount.removeItem(int(0))
        self.parent().comboChooseAccount.addItem(sAccName)

class UserInterface(QtWidgets.QMainWindow, Ui_PyMoneyOrgaGui):
    """implementation of the PyMoneyOrga Gui"""
    
    def __init__(self, cDatabase, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.modelTableViewAccounts = QtGui.QStandardItemModel()
        self.modelTableViewAccounts.setColumnCount(2)
        headerNames = []
        headerNames.append("Account")
        headerNames.append("Money")
        self.modelTableViewAccounts.setHorizontalHeaderLabels(headerNames)
        self.tableViewAccounts.setModel(self.modelTableViewAccounts)
        self.cDatabase = cDatabase
        self.dialogCreateNewAccount = None

		# Connect menu button with a custom function (openDialogCreatNewAccount)
        self.actionCreate_New_Account.triggered.connect(self.openDialogCreatNewAccount)

        # Connect new expenses button with a custom function (addNewExpenses)
        self.buttonAddExpenses.clicked.connect(self.addNewExpenses)
        
    
    def updateTableViewAccounts(self):
        for row in range(self.modelTableViewAccounts.rowCount()):
            indexAccName = self.modelTableViewAccounts.index(row, 0)
            sAccName = self.modelTableViewAccounts.data(indexAccName)
            indexCash = self.modelTableViewAccounts.index(row, 1)
            self.modelTableViewAccounts.setData(indexCash, self.cDatabase.acAllAccs[sAccName].getCash())


            
    def openDialogCreatNewAccount(self):
        if self.dialogCreateNewAccount is None:
            self.dialogCreateNewAccount = DialogCreatNewAccount(self)
            self.dialogCreateNewAccount.show()

    def addNewExpenses(self):
        sAccName = self.comboChooseAccount.currentText()
        iExpenses = int(self.inputAddExpenses.text())
        self.cDatabase.acAllAccs[sAccName].addExpenses(iExpenses)
        self.updateTableViewAccounts()
    