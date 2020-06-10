import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from .gui.PyMoneyOrgaGui import Ui_PyMoneyOrgaGui
from .gui.dialogCreateNewAccount import Ui_dialogCreateNewAccount
from .account import Account
from .database.database import Database


class DialogCreatNewAccount(QtWidgets.QDialog, Ui_dialogCreateNewAccount):
    """implementation of the dialogCreateNewAccount Gui"""
    
    def __init__(self, parent=None):
        super(DialogCreatNewAccount, self).__init__(parent)
        self.setupUi(self)
        # Connect add button with a custom function (addAcc)
        self.buttonAddNewAccount.clicked.connect(self.add_acc)


    def closeEvent(self, event):
        self.parent().dialog_create_new_acc = None
        

    def add_acc(self):
        acc_name = str(self.inputAccountName.text())
        balance = int(self.inputInitialAmount.text())
        new_acc = Account(acc_name, balance)
        self.parent().database.add_acc(new_acc)
        
        item_acc_name = QtGui.QStandardItem(acc_name)
        item_acc_name.setEditable(False)
        item_balance = QtGui.QStandardItem(str(balance))
        item_balance.setEditable(False)
        row = [item_acc_name,item_balance]
        self.parent().model_table_view_accounts.appendRow(row)
        self.parent().buttonAddExpenses.setEnabled(True)

        for account in self.parent().database.dict_all_acc.values():
            print(account)

        # delete the initial combo box item and add a new one for the account 
        if self.parent().comboChooseAccount.currentText() == "NoAccountSaved":
            self.parent().comboChooseAccount.removeItem(int(0))
        self.parent().comboChooseAccount.addItem(acc_name)

class UserInterface(QtWidgets.QMainWindow, Ui_PyMoneyOrgaGui):
    """implementation of the PyMoneyOrga Gui"""
    
    def __init__(self, database, parent=None):
        super(UserInterface, self).__init__(parent)
        self.setupUi(self)
        self.model_table_view_accounts = QtGui.QStandardItemModel()
        self.model_table_view_accounts.setColumnCount(2)
        header_names = []
        header_names.append("Account")
        header_names.append("Money")
        self.model_table_view_accounts.setHorizontalHeaderLabels(header_names)
        self.tableViewAccounts.setModel(self.model_table_view_accounts)
        self.database = database
        self.dialog_create_new_acc = None

		# Connect menu button with a custom function (openDialogCreatNewAccount)
        self.actionCreate_New_Account.triggered.connect(self.open_dialog_creat_new_acc)

        # Connect new expenses button with a custom function (addNewExpenses)
        self.buttonAddExpenses.clicked.connect(self.add_new_expenses)

        if not self.database.dict_all_acc:
            self.buttonAddExpenses.setEnabled(False)
            
    
    def update_table_view_accounts(self):
        for row in range(self.model_table_view_accounts.rowCount()):
            index_acc_name = self.model_table_view_accounts.index(row, 0)
            acc_name = self.model_table_view_accounts.data(index_acc_name)
            index_balance = self.model_table_view_accounts.index(row, 1)
            self.model_table_view_accounts.setData(index_balance, self.database.dict_all_acc[acc_name].balance)

            
    def open_dialog_creat_new_acc(self):
        if self.dialog_create_new_acc is None:
            self.dialog_create_new_acc = DialogCreatNewAccount(self)
            self.dialog_create_new_acc.show()


    def add_new_expenses(self):
        acc_name = self.comboChooseAccount.currentText()
        expenses = int(self.inputAddExpenses.text()) if self.inputAddExpenses.text() != '' else 0
        self.database.dict_all_acc[acc_name].add_expenses(expenses)
        self.update_table_view_accounts()
    