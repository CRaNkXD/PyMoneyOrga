from PySide2 import QtCore, QtWidgets
from PySide2.QtCharts import QtCharts
from .gui.PyMoneyOrgaGui import Ui_PyMoneyOrgaGui
from .dialogs.dialogDeleteAccount import DialogDeleteAccount
from .dialogs.dialogCreateNewAccount import DialogCreateNewAccount

from .service_layer import services_account
from .database.database_interface import DatabaseInterface


class MainWindow(QtWidgets.QMainWindow, Ui_PyMoneyOrgaGui):
    """implementation of the PyMoneyOrga Gui"""

    def __init__(self, database: DatabaseInterface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.tableWidgetTransactions.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )
        self.tableWidgetAccounts.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )

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

        self.tabWidget.setCurrentIndex(0)

    def init_gui_with_database(self):
        accs = services_account.get_all_acc(self.database)
        self.init_table_accounts(accs)
        self.init_comboChooseAccount(accs)
        self.init_table_transactions()
        self.init_chart()
        if not accs:
            self.buttonAddExpenses.setEnabled(False)
            self.buttonAddIncome.setEnabled(False)
        else:
            self.buttonAddExpenses.setEnabled(True)
            self.buttonAddIncome.setEnabled(True)

    def init_comboChooseAccount(self, accs):
        if accs:
            self.comboChooseAccount.clear()
            for acc in accs:
                self.comboChooseAccount.addItem(acc.acc_name)
        else:
            self.comboChooseAccount.clear()
            self.comboChooseAccount.addItem("NoAccountSaved")

    def init_table_accounts(self, accs):
        if accs:
            self.tableWidgetAccounts.setRowCount(len(accs))
            currentRowCount = 0
            for acc in accs:
                item_acc_name = QtWidgets.QTableWidgetItem(acc.acc_name)
                self.tableWidgetAccounts.setItem(currentRowCount, 0, item_acc_name)
                item_balance = QtWidgets.QTableWidgetItem()
                item_balance.setData(QtCore.Qt.DisplayRole, acc.balance)
                self.tableWidgetAccounts.setItem(currentRowCount, 1, item_balance)
                currentRowCount += 1
        else:
            self.tableWidgetAccounts.setRowCount(0)

    def init_table_transactions(self):
        current_acc = self.comboChooseAccount.currentText()
        transactions = services_account.get_transactions(self.database, current_acc)
        if transactions != []:
            self.tableWidgetTransactions.setRowCount(len(transactions))
            currentRowCount = 0
            for transaction in transactions:
                item_time_stamp = QtWidgets.QTableWidgetItem()
                item_time_stamp.setData(
                    QtCore.Qt.DisplayRole,
                    transaction.time_stamp.strftime("%d/%m/%y - %H:%M:%S"),
                )
                self.tableWidgetTransactions.setItem(
                    currentRowCount, 0, item_time_stamp
                )
                item_amount = QtWidgets.QTableWidgetItem()
                item_amount.setData(QtCore.Qt.DisplayRole, transaction.amount)
                self.tableWidgetTransactions.setItem(currentRowCount, 1, item_amount)
                item_new_balance = QtWidgets.QTableWidgetItem()
                item_new_balance.setData(QtCore.Qt.DisplayRole, transaction.new_balance)
                self.tableWidgetTransactions.setItem(
                    currentRowCount, 2, item_new_balance
                )
                item_description = QtWidgets.QTableWidgetItem(
                    str(transaction.description)
                )
                self.tableWidgetTransactions.setItem(
                    currentRowCount, 3, item_description
                )
                currentRowCount += 1
        else:
            self.tableWidgetTransactions.setRowCount(0)

    def setup_chart(self):
        """
        setup the chart view by adding it to the widgetChart used as a
        place holder in the qt designer
        """
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
        # self.axis_x.setLabelFormat("dd.MM (h:mm)")
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
        transactions = services_account.get_transactions(self.database, current_acc)
        self.series.clear()
        if transactions != []:
            # x_max = transactions[0].id
            # x_min = transactions[0].id
            y_min = transactions[0].new_balance
            y_max = transactions[0].new_balance
            x = 0
            for transaction in transactions:
                # x = transaction.id
                x += 1
                y = transaction.new_balance
                # x_max = max(x_max, x)
                # x_min = min(x_min, x)
                y_max = max(y_max, y)
                y_min = min(y_min, y)
                self.series.append(x, y)

            # self.axis_x.setMin(x_min)
            # self.axis_x.setMax(x_max)
            self.axis_x.setMin(0)
            self.axis_x.setMax(x)
            self.axis_y.setMin(y_min)
            self.axis_y.setMax(y_max)

        self.chartview.repaint()

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
        if self.inputAddExpenses.text() != "":
            expense = int(self.inputAddExpenses.text())
        else:
            return

        description = (
            self.inputDescriptionExpenses.text()
            if self.inputDescriptionExpenses.text() != ""
            else "expense"
        )
        services_account.add_expense(self.database, acc_name, expense, description)
        accs = services_account.get_all_acc(self.database)
        self.init_table_accounts(accs)
        self.init_table_transactions()
        self.init_chart()

    def add_new_income(self):
        acc_name = self.comboChooseAccount.currentText()
        if self.inputAddIncome.text() != "":
            income = int(self.inputAddIncome.text())
        else:
            return

        description = (
            self.inputDescriptionIncome.text()
            if self.inputDescriptionIncome.text() != ""
            else "income"
        )
        services_account.add_income(self.database, acc_name, income, description)
        accs = services_account.get_all_acc(self.database)
        self.init_table_accounts(accs)
        self.init_table_transactions()
        self.init_chart()
