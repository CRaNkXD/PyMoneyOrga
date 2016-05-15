import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from .gui.PyMoneyOrgaGui import Ui_PyMoneyOrgaGui
from .gui.dialogCreateNewAccount import Ui_dialogCreateNewAccount
from .account import Account
from .database import Database


class DialogCreatNewAccount(QtWidgets.QDialog, Ui_dialogCreateNewAccount):
    def __init__(self, dialogCreateNewAccount, parent):
        super().__init__(parent=parent)
        self.setupUi(dialogCreateNewAccount)
        # Connect add button with a custom function (addAcc)
        self.buttonAddNewAccount.clicked.connect(self.addAcc)

    def addAcc(self):
        sAccName = str(self.inputAccountName.text())
        iCash = str(self.inputInitialAmount.text())
        cNewAcc = Account(sAccName, iCash)
        self.parent().cDatabase.addAcc(cNewAcc)
        itemAccName = QtGui.QStandardItem(sAccName)
        itemAccName.setEditable(False)
        itemCash = QtGui.QStandardItem(iCash)
        itemCash.setEditable(False)
        row = [itemAccName,itemCash]
        self.parent().model.appendRow(row)

class UserInterface(QtWidgets.QMainWindow, Ui_PyMoneyOrgaGui):
    """implementation of the PyMoneyOrga Gui"""
    
    def __init__(self, PyMoneyOrgaGui, cDatabase, parent=None):
        super().__init__(parent)
        self.setupUi(PyMoneyOrgaGui)
        self.model = QtGui.QStandardItemModel()
        self.model.setColumnCount(2)
        headerNames = []
        headerNames.append("Account")
        headerNames.append("Money")
        self.model.setHorizontalHeaderLabels(headerNames)
        self.tableViewAccounts.setModel(self.model)
        self.cDatabase = cDatabase
        self.dialogCreateNewAccount = None

		# Connect menu button with a custom function (addAcc)
        self.actionCreate_New_Account.triggered.connect(self.openDialogCreatNewAccount)
    
        
    def openDialogCreatNewAccount(self):
        wDialogCreateNewAccount = QtWidgets.QDialog()
        self.dialogCreateNewAccount = DialogCreatNewAccount(wDialogCreateNewAccount, self)
        self.dialogCreateNewAccount.show()
     