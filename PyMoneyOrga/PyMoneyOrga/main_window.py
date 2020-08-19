from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCharts import QtCharts
from .gui.UIPyMoneyOrgaGui import Ui_PyMoneyOrgaGui
from .gui.float_delegate import FloatDelegate
from .dialogs.dialogDeleteAccount import DialogDeleteAccount
from .dialogs.dialogCreateNewAccount import DialogCreateNewAccount

from .service_layer import services_account
from .service_layer import services_gui
from .database.database_interface import DatabaseInterface


class MainWindow(QtWidgets.QMainWindow, Ui_PyMoneyOrgaGui):
    """implementation of the PyMoneyOrga Gui"""

    __COLUMN_TIMESTAMP = 0
    __COLUMN_AMOUNT = 1
    __COLUMN_NEWBALANCE = 2
    __COLUMN_DESCRIPTION = 3

    def __init__(self, database: DatabaseInterface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # set the tables to not editable
        self.tableWidgetTransactions.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )
        self.tableWidgetAccounts.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )

        # set the tables text format
        self.tableWidgetAccounts.setItemDelegateForColumn(1, FloatDelegate())
        # self.tableWidgetTransactions.setItemDelegateForColumn(self.__COLUMN_NEWBALANCE, FloatDelegate())
        self.tableWidgetTransactions.setItemDelegateForColumn(
            self.__COLUMN_AMOUNT, FloatDelegate()
        )

        # set the line edit so it only accepts double values
        dvExpenses = QtGui.QDoubleValidator(0.0, 10.0 ** 100, 2, self.inputAddExpenses)
        dvExpenses.setNotation(QtGui.QDoubleValidator.StandardNotation)
        dvIncome = QtGui.QDoubleValidator(0.0, 10.0 ** 100, 2, self.inputAddIncome)
        dvIncome.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.inputAddExpenses.setValidator(dvExpenses)
        self.inputAddIncome.setValidator(dvIncome)

        self.database = database
        # variables for storing new windows
        # windows can only be opened when the variable is None
        # like this only one window of the same kind can be opened at the same time
        self.dialog_create_new_acc = None
        self.dialog_delete_acc = None

        # connect the buttons with the methods
        self.actionCreate_New_Account.triggered.connect(self.open_dialog_create_new_acc)
        self.actionDeleteAccount.triggered.connect(self.open_dialog_delete_acc)
        self.actionExit.triggered.connect(self.close)
        self.buttonAddExpenses.clicked.connect(self.add_new_expenses)
        self.buttonAddIncome.clicked.connect(self.add_new_income)
        self.comboChooseAccount.currentTextChanged.connect(self.init_table_transactions)
        self.comboChooseAccount.currentTextChanged.connect(self.init_chart)
        self.checkShowAmount.stateChanged.connect(
            lambda state: self.toggle_transaction_table_column_vis(
                state, self.__COLUMN_AMOUNT
            )
        )
        self.checkShowDescription.stateChanged.connect(
            lambda state: self.toggle_transaction_table_column_vis(
                state, self.__COLUMN_DESCRIPTION
            )
        )
        self.checkShowNewBalance.stateChanged.connect(
            lambda state: self.toggle_transaction_table_column_vis(
                state, self.__COLUMN_NEWBALANCE
            )
        )
        self.checkShowTimeStamp.stateChanged.connect(
            lambda state: self.toggle_transaction_table_column_vis(
                state, self.__COLUMN_TIMESTAMP
            )
        )

        self._setup_chart()

        self.init_gui_with_database()

        self.tabWidget.setCurrentIndex(0)

    def init_gui_with_database(self):
        """
        initialze the whole gui with the database
        """
        accs = services_account.get_all_acc(self.database)
        self.init_table_accounts(accs)
        self.init_comboChooseAccount(accs)
        self.init_table_transactions()
        self.init_chart()
        if not accs:
            # if no accounts are saved it is not possible to add income or expense
            self.enable_buttons(False)
        else:
            self.enable_buttons(True)

    def enable_buttons(self, enable):
        self.buttonAddExpenses.setEnabled(enable)
        self.buttonAddIncome.setEnabled(enable)

    def init_comboChooseAccount(self, accs):
        """
        initialze the comboChooseAccount with the accounts from the database
        """
        if accs:
            self.comboChooseAccount.clear()
            for acc in accs:
                self.comboChooseAccount.addItem(acc.acc_name)
        else:
            self.comboChooseAccount.clear()
            self.comboChooseAccount.addItem("NoAccountSaved")

    def init_table_accounts(self, accs):
        """
        initialize the account table with the database
        """
        if accs:
            self.tableWidgetAccounts.setRowCount(len(accs))
            currentRowCount = 0
            for acc in accs:
                item_acc_name = QtWidgets.QTableWidgetItem(acc.acc_name)
                self.tableWidgetAccounts.setItem(currentRowCount, 0, item_acc_name)
                item_balance = QtWidgets.QTableWidgetItem()
                item_balance.setData(QtCore.Qt.DisplayRole, acc.balance / 100)
                self.tableWidgetAccounts.setItem(currentRowCount, 1, item_balance)
                currentRowCount += 1
        else:
            self.tableWidgetAccounts.setRowCount(0)

    def init_table_transactions(self):
        """
        initialize the transaction table for the specified account with the database
        account specified by the comboChooseAccount
        """
        current_acc = self.comboChooseAccount.currentText()
        transactions = services_account.get_transactions(
            self.database, current_acc, max_length=20, reverse=True
        )
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
                    currentRowCount, self.__COLUMN_TIMESTAMP, item_time_stamp
                )
                item_amount = QtWidgets.QTableWidgetItem()
                item_amount.setData(QtCore.Qt.DisplayRole, transaction.amount / 100)
                self.tableWidgetTransactions.setItem(
                    currentRowCount, self.__COLUMN_AMOUNT, item_amount
                )
                item_new_balance = QtWidgets.QTableWidgetItem()
                item_new_balance.setData(
                    QtCore.Qt.DisplayRole, transaction.new_balance / 100
                )
                self.tableWidgetTransactions.setItem(
                    currentRowCount, self.__COLUMN_NEWBALANCE, item_new_balance
                )
                item_description = QtWidgets.QTableWidgetItem(
                    str(transaction.description)
                )
                self.tableWidgetTransactions.setItem(
                    currentRowCount, self.__COLUMN_DESCRIPTION, item_description
                )
                currentRowCount += 1
        else:
            self.tableWidgetTransactions.setRowCount(0)

    def _setup_chart(self):
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
        self.axis_x.setTitleText("Transaction")
        self.series.attachAxis(self.axis_x)

        # Y Axis Settings
        self.axis_y = QtCharts.QValueAxis()
        self.chart.addAxis(self.axis_y, QtCore.Qt.AlignLeft)
        self.axis_y.setTitleText("Balance in EUR")
        self.series.attachAxis(self.axis_y)

        # add hovering tooltips
        self.point_tool_tip_dict = {}
        self.series.hovered.connect(self.show_point_tooltip)

        self.chartview.setChart(self.chart)

    def init_chart(self):
        """
        initialize the data for the chart view
        """
        current_acc = self.comboChooseAccount.currentText()
        transactions = services_account.get_transactions(self.database, current_acc)
        self.series.clear()
        if transactions != []:
            # initialize the graph with the starting balance
            x = 0
            y = transactions[0].new_balance / 100 - transactions[0].amount / 100
            self.series.append(x, y)

            y_min = transactions[0].new_balance / 100 - transactions[0].amount / 100
            y_max = transactions[0].new_balance / 100 - transactions[0].amount / 100
            for transaction in transactions:
                x += 1
                y = transaction.new_balance / 100
                y_max = max(y_max, y)
                y_min = min(y_min, y)
                self.series.append(x, y)

            self.axis_x.setMin(0)
            self.axis_x.setMax(x)
            self.axis_y.setMin(y_min)
            self.axis_y.setMax(y_max)

            self.series.setPointsVisible(True)

        self.chartview.repaint()

    def open_dialog_create_new_acc(self):
        """
        opens the dialog for creating a new account
        """
        if self.dialog_create_new_acc is None:
            self.dialog_create_new_acc = DialogCreateNewAccount(self)
            self.dialog_create_new_acc.show()

    def open_dialog_delete_acc(self):
        """
        opens the dialog for deleting an account
        """
        if self.dialog_delete_acc is None:
            self.dialog_delete_acc = DialogDeleteAccount(self)
            self.dialog_delete_acc.show()

    def add_new_expenses(self):
        """
        adds an expense to an account
        expense sepccifed by the inputAddExpenses
        account specified by the comboChooseAccount
        """
        acc_name = self.comboChooseAccount.currentText()
        expense = self.inputAddExpenses.text()
        if expense == "":
            services_gui.show_info_msg_box("The amount is not specified!")
            return

        description = (
            self.inputDescriptionExpenses.text()
            if self.inputDescriptionExpenses.text() != ""
            else "expense"
        )
        expense = int(float(expense.replace(",", ".")) * 100)
        services_account.add_expense(self.database, acc_name, expense, description)
        accs = services_account.get_all_acc(self.database)
        self.init_table_accounts(accs)
        self.init_table_transactions()
        self.init_chart()

    def add_new_income(self):
        """
        adds an income to an account
        income sepccifed by the inputAddIncome
        account specified by the comboChooseAccount
        """
        acc_name = self.comboChooseAccount.currentText()
        income = self.inputAddIncome.text()
        if income == "":
            services_gui.show_info_msg_box("The amount is not specified!")
            return

        description = (
            self.inputDescriptionIncome.text()
            if self.inputDescriptionIncome.text() != ""
            else "income"
        )
        income = int(float(income.replace(",", ".")) * 100)
        services_account.add_income(self.database, acc_name, income, description)
        accs = services_account.get_all_acc(self.database)
        self.init_table_accounts(accs)
        self.init_table_transactions()
        self.init_chart()

    def toggle_transaction_table_column_vis(self, state, column):
        if state == 0:
            self.tableWidgetTransactions.setColumnHidden(column, True)
        else:
            self.tableWidgetTransactions.setColumnHidden(column, False)

    def show_point_tooltip(self, point: QtCore.QPointF, state: bool):
        point_coord = self.chart.mapToPosition(point)
        point_coord = self.chart.mapToScene(point_coord)
        mouse_box = QtCore.QRect(
            point_coord.toPoint() - QtCore.QPoint(10, 10),
            point_coord.toPoint() + QtCore.QPoint(10, 10),
        )
        # print(mouse_box)
        for data_point in self.series.points():
            data_point_coord = self.chart.mapToPosition(data_point)
            data_point_coord = self.chart.mapToScene(data_point_coord)
            if mouse_box.contains(data_point_coord.toPoint()):
                if (
                    str(data_point_coord) not in self.point_tool_tip_dict
                    and self.point_tool_tip_dict
                ):
                    # print("remove item")
                    # print(data_point.toPoint())
                    for key in self.point_tool_tip_dict:
                        self.chart.scene().removeItem(self.point_tool_tip_dict[key])

                    self.point_tool_tip_dict = {}

                if not self.point_tool_tip_dict:
                    # print(data_point.toPoint())
                    point_tool_tip = QtWidgets.QGraphicsSimpleTextItem()
                    point_tool_tip.setText(
                        "Transaction: "
                        + str(data_point.toPoint().x())
                        + " "
                        + "Balance: "
                        + str(data_point.toPoint().y())
                    )

                    point_tool_tip.setPos(data_point_coord - QtCore.QPoint(30, 30))
                    # print("add item")
                    self.chart.scene().addItem(point_tool_tip)
                    self.point_tool_tip_dict[str(data_point_coord)] = point_tool_tip
                break
