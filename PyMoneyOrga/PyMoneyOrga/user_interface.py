import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCharts import QtCharts
from .gui.PyMoneyOrgaGui import Ui_PyMoneyOrgaGui
from .dialogs.dialogDeleteAccount import DialogDeleteAccount
from .dialogs.dialogCreateNewAccount import DialogCreateNewAccount

from .account import Account


class UserInterface(QtWidgets.QMainWindow, Ui_PyMoneyOrgaGui):
    """implementation of the PyMoneyOrga Gui"""
    
    def __init__(self, database, parent=None):
        super(UserInterface, self).__init__(parent)
        self.setupUi(self)

        self.tableWidgetTransactions.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetAccounts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.database = database
        self.dialog_create_new_acc = None
        self.dialog_delete_acc = None

		# Connect menu button with a custom function (openDialogCreateNewAccount)
        self.actionCreate_New_Account.triggered.connect(self.open_dialog_create_new_acc)

        # Connect menu button with a custom function (openDialogDeleteAccount)
        self.actionDeleteAccount.triggered.connect(self.open_dialog_delete_acc)

        self.actionExit.triggered.connect(self.close)

        # Connect new expenses button with a custom function (addNewExpenses)
        self.buttonAddExpenses.clicked.connect(self.add_new_expenses)

        # Connect new income button with a custom function (addNewIncome)
        self.buttonAddIncome.clicked.connect(self.add_new_income)

        self.comboChooseAccount.currentTextChanged.connect(self.init_table_transactions)
        self.comboChooseAccount.currentTextChanged.connect(self.init_chart)

        self.setup_chart()
                                            
        self.init_gui_with_database()

    
    def init_gui_with_database(self):
        accs_dict = self.database.get_all_acc()
        self.init_table_accounts(accs_dict)
        self.init_comboChooseAccount(accs_dict)
        self.init_table_transactions()
        self.init_chart()
        if not accs_dict:
            self.buttonAddExpenses.setEnabled(False)
            self.buttonAddIncome.setEnabled(False)
        else:
            self.buttonAddExpenses.setEnabled(True)
            self.buttonAddIncome.setEnabled(True)


    def init_comboChooseAccount(self, accs_dict):
        if accs_dict != {}:
            self.comboChooseAccount.clear()
            for acc_name in accs_dict.keys():
                self.comboChooseAccount.addItem(acc_name)
        else:
            self.comboChooseAccount.clear()
            self.comboChooseAccount.addItem("NoAccountSaved")
            

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
                item_description = QtWidgets.QTableWidgetItem(str(transaction.description))
                self.tableWidgetTransactions.setItem(currentRowCount, 3, item_description)
                currentRowCount += 1
        else:
            self.tableWidgetTransactions.setRowCount(0)


    def setup_chart(self):
        # setup the chart view by adding it to the widgetChart used as a place holder in the qt designer
        self.widgetChart.setContentsMargins(0, 0, 0, 0)
        lay = QtWidgets.QVBoxLayout(self.widgetChart)
        lay.setContentsMargins(0, 0, 0, 0)

        self.chartview = QtCharts.QChartView()
        self.chartview.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.chartview)

        # init data series for chart
        self.series = QtCharts.QLineSeries()

        # Create Chart and set General Chart setting
        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        # X Axis Settings
        self.axis_x = QtCharts.QValueAxis()
        self.chart.addAxis(self.axis_x, QtCore.Qt.AlignBottom)
        #self.axis_x.setLabelFormat("dd.MM (h:mm)")
        self.axis_x.setTitleText("Date")
        self.series.attachAxis(self.axis_x)

        # Y Axis Settings
        self.axis_y = QtCharts.QValueAxis()
        self.chart.addAxis(self.axis_y, QtCore.Qt.AlignLeft)
        self.axis_y.setTitleText("Balance")
        self.series.attachAxis(self.axis_y)

        self.chartview.setChart(self.chart)


    def init_chart(self):
        # initialize the data for the chart view
        current_acc = self.comboChooseAccount.currentText()
        transactions = self.database.get_all_transaction(current_acc)
        self.series.clear()
        x_max = transactions[0].id
        x_min = transactions[0].id
        y_min = transactions[0].new_balance
        y_max = transactions[0].new_balance
        for transaction in transactions:
            x = transaction.id
            y = transaction.new_balance
            x_max = max(x_max, x)
            y_max = max(y_max, y)
            x_min = min(x_min, x)
            y_min = min(y_min, y)
            self.series.append(x, y)
        
        self.axis_x.setMin(x_min)
        self.axis_x.setMax(x_max)
        self.axis_y.setMin(y_min)
        self.axis_y.setMax(y_max)
        self.chartview.repaint()


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
            item_description = QtWidgets.QTableWidgetItem(str(transaction.description))
            self.tableWidgetTransactions.setItem(currentRowCount - 1, 3, item_description)


    def init_table_accounts(self, accs_dict):
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

     
    def open_dialog_create_new_acc(self):
        if self.dialog_create_new_acc is None:
            self.dialog_create_new_acc = DialogCreateNewAccount(self)
            self.dialog_create_new_acc.show()


    def open_dialog_delete_acc(self):
        if self.dialog_delete_acc is None:
            self.dialog_delete_acc = DialogDeleteAccount(self)
            self.dialog_delete_acc.show()


    def add_new_expenses(self):
        acc_name = self.comboChooseAccount.currentText()
        expenses = int(self.inputAddExpenses.text()) if self.inputAddExpenses.text() != '' else 0
        description = self.inputDescriptionExpenses.text() if self.inputDescriptionExpenses.text() != '' else "expense"
        acc = self.database.get_acc(acc_name)
        acc = Account(acc_name,acc[acc_name])
        acc.add_expenses(expenses)
        self.database.update_acc_balance(acc_name, acc.balance)
        time_stamp = self.database.add_transaction(acc_name, -expenses, acc.balance, description)
        self.update_table_accounts_balance(acc_name, acc.balance)
        self.add_item_table_transactions(time_stamp)
        self.init_chart()


    def add_new_income(self):
        acc_name = self.comboChooseAccount.currentText()
        income = int(self.inputAddIncome.text()) if self.inputAddIncome.text() != '' else 0
        description = self.inputDescriptionIncome.text() if self.inputDescriptionIncome.text() != '' else "income"
        acc = self.database.get_acc(acc_name)
        acc = Account(acc_name,acc[acc_name])
        acc.add_income(income)
        self.database.update_acc_balance(acc_name, acc.balance)
        time_stamp = self.database.add_transaction(acc_name, income, acc.balance, description)
        self.update_table_accounts_balance(acc_name, acc.balance)
        self.add_item_table_transactions(time_stamp)
        self.init_chart()
