import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from .gui.PyMoneyOrgaGui import Ui_PyMoneyOrgaGui
from .gui.dialogCreateNewAccount import Ui_dialogCreateNewAccount
from .account import Account


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
        self.parent().database.add_acc(acc_name, balance)
        
        currentRowCount = self.parent().tableWidgetAccounts.rowCount() + 1
        self.parent().tableWidgetAccounts.setRowCount(currentRowCount)
        
        item_acc_name = QtWidgets.QTableWidgetItem(acc_name)
        self.parent().tableWidgetAccounts.setItem(currentRowCount - 1, 0, item_acc_name)
        item_balance = QtWidgets.QTableWidgetItem(str(balance))
        self.parent().tableWidgetAccounts.setItem(currentRowCount - 1, 1, item_balance)


        # delete the initial combo box item and add a new one for the account 
        if self.parent().comboChooseAccount.currentText() == "NoAccountSaved":
            self.parent().comboChooseAccount.removeItem(int(0))
        self.parent().comboChooseAccount.addItem(acc_name)

class UserInterface(QtWidgets.QMainWindow, Ui_PyMoneyOrgaGui):
    """implementation of the PyMoneyOrga Gui"""
    
    def __init__(self, database, parent=None):
        super(UserInterface, self).__init__(parent)
        self.setupUi(self)
        #self.model_table_view_accounts = QtGui.QStandardItemModel()
        #self.model_table_view_accounts.setColumnCount(2)
        #header_names_accounts = []
        #header_names_accounts.append("Account")
        #header_names_accounts.append("Balance")
        #self.model_table_view_accounts.setHorizontalHeaderLabels(header_names_accounts)
        #self.tableViewAccounts.setModel(self.model_table_view_accounts)

        #header_names_transactions = []
        #header_names_transactions.append("Time stamp")
        #header_names_transactions.append("Amount")
        #header_names_transactions.append("New balance")
        #self.tableWidgetTransactions.setColumnCount(len(header_names_transactions))
        #self.tableWidgetTransactions.setHorizontalHeaderLabels(header_names_transactions)
        # set the cells in the table widget to read only
        self.tableWidgetTransactions.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetAccounts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.database = database
        self.dialog_create_new_acc = None

		# Connect menu button with a custom function (openDialogCreatNewAccount)
        self.actionCreate_New_Account.triggered.connect(self.open_dialog_creat_new_acc)

        self.actionExit.triggered.connect(self.close)

        # Connect new expenses button with a custom function (addNewExpenses)
        self.buttonAddExpenses.clicked.connect(self.add_new_expenses)

        # Connect new income button with a custom function (addNewIncome)
        self.buttonAddIncome.clicked.connect(self.add_new_income)

        self.comboChooseAccount.currentTextChanged.connect(self.init_table_transactions)
                                            
        accs_dict = self.init_gui_with_database()

        if not accs_dict:
            self.buttonAddExpenses.setEnabled(False)
            
    
    def init_gui_with_database(self):
        accs_dict = self.database.get_all_acc()
        if accs_dict != {}:
            self.comboChooseAccount.removeItem(int(0))

        self.init_table_accounts()
        self.init_table_transactions()
        return accs_dict


    def init_table_transactions(self):
        current_acc = self.comboChooseAccount.currentText()
        transactions = self.database.get_all_transaction(current_acc)
        if transactions != []:
            self.tableWidgetTransactions.setRowCount(len(transactions))
            currentRowCount = 0
            for transaction in transactions:
                item_time_stamp = QtWidgets.QTableWidgetItem(str(transaction.time_stamp))
                self.tableWidgetTransactions.setItem(currentRowCount, 0, item_time_stamp)
                item_amount = QtWidgets.QTableWidgetItem(str(transaction.amount))
                self.tableWidgetTransactions.setItem(currentRowCount, 1, item_amount)
                item_new_balance = QtWidgets.QTableWidgetItem(str(transaction.new_balance))
                self.tableWidgetTransactions.setItem(currentRowCount, 2, item_new_balance)
                currentRowCount += 1
        else:
            self.tableWidgetTransactions.setRowCount(0)


    def add_item_table_transactions(self, time_stamp):
        """ add an item to the transactions table from the database using the specific time stamp as identifier """
        current_acc = self.comboChooseAccount.currentText()
        transaction = self.database.get_transaction(current_acc, time_stamp)
        if transaction != None:
            currentRowCount = self.tableWidgetTransactions.rowCount() + 1
            self.tableWidgetTransactions.setRowCount(currentRowCount)
            item_time_stamp = QtWidgets.QTableWidgetItem(str(transaction.time_stamp))
            self.tableWidgetTransactions.setItem(currentRowCount - 1, 0, item_time_stamp)
            item_amount = QtWidgets.QTableWidgetItem(str(transaction.amount))
            self.tableWidgetTransactions.setItem(currentRowCount - 1, 1, item_amount)
            item_new_balance = QtWidgets.QTableWidgetItem(str(transaction.new_balance))
            self.tableWidgetTransactions.setItem(currentRowCount - 1, 2, item_new_balance)


    def init_table_accounts(self):
        accs_dict = self.database.get_all_acc()
        if accs_dict != {}:
            self.tableWidgetAccounts.setRowCount(len(accs_dict))
            currentRowCount = 0
            for acc_name, balance in accs_dict.items():
                self.comboChooseAccount.addItem(acc_name)
                item_acc_name = QtWidgets.QTableWidgetItem(acc_name)
                self.tableWidgetAccounts.setItem(currentRowCount, 0, item_acc_name)
                item_balance = QtWidgets.QTableWidgetItem(str(balance))
                self.tableWidgetAccounts.setItem(currentRowCount, 1, item_balance)
                currentRowCount += 1

        else:
            self.tableWidgetAccounts.setRowCount(0)


    def update_table_accounts_balance(self, acc_name, balance):
        for row in range(self.tableWidgetAccounts.rowCount()):
            item_acc_name = self.tableWidgetAccounts.item(row, 0)
            local_acc_name = item_acc_name.text()
            if acc_name == local_acc_name:
                item_balance = self.tableWidgetAccounts.item(row, 1)
                item_balance.setText(str(balance))

     
    def open_dialog_creat_new_acc(self):
        if self.dialog_create_new_acc is None:
            self.dialog_create_new_acc = DialogCreatNewAccount(self)
            self.dialog_create_new_acc.show()


    def add_new_expenses(self):
        acc_name = self.comboChooseAccount.currentText()
        expenses = int(self.inputAddExpenses.text()) if self.inputAddExpenses.text() != '' else 0
        acc = self.database.get_acc(acc_name)
        acc = Account(acc_name,acc[acc_name])
        acc.add_expenses(expenses)
        self.database.update_acc_balance(acc_name, acc.balance)
        time_stamp = self.database.add_transaction(acc_name, -expenses, acc.balance)
        self.update_table_accounts_balance(acc_name, acc.balance)
        self.add_item_table_transactions(time_stamp)


    def add_new_income(self):
        acc_name = self.comboChooseAccount.currentText()
        income = int(self.inputAddIncome.text()) if self.inputAddIncome.text() != '' else 0
        acc = self.database.get_acc(acc_name)
        acc = Account(acc_name,acc[acc_name])
        acc.add_cash(income)
        self.database.update_acc_balance(acc_name, acc.balance)
        time_stamp = self.database.add_transaction(acc_name, income, acc.balance)
        self.update_table_accounts_balance(acc_name, acc.balance)
        self.add_item_table_transactions(time_stamp)
