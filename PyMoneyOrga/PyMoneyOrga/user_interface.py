import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from .gui.PyMoneyOrgaGui import Ui_PyMoneyOrgaGui
from .account import Account
from .database import Database

class UserInterface(Ui_PyMoneyOrgaGui):
    """implementation of the PyMoneyOrga Gui"""
    
    def __init__(self, PyMoneyOrgaGui, cDatabase):
        Ui_PyMoneyOrgaGui.__init__(self)
        self.setupUi(PyMoneyOrgaGui)
        self.model = QtGui.QStandardItemModel()
        self.model.setColumnCount(2)
        headerNames = []
        headerNames.append("Account")
        headerNames.append("Money")
        self.model.setHorizontalHeaderLabels(headerNames)
        self.tableViewAccounts.setModel(self.model)
        self.cDatabase = cDatabase
        

		# Connect add button with a custom function (addAcc)
        self.buttonAddNewAccount.clicked.connect(self.addAcc)
    
    def addAcc(self):
        sAccName = str(self.inputAccountName.text())
        iCash = int(self.inputInitialAmount.text())
        cNewAcc = Account(sAccName, iCash)
        self.cDatabase.addAcc(cNewAcc)
        itemAccName = QtGui.QStandardItem(sAccName)
        itemAccName.setEditable(False)
        itemCash = QtGui.QStandardItem(str(iCash))
        itemCash.setEditable(False)
        row = [itemAccName,itemCash]
        self.model.appendRow(row)