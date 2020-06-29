from PySide2 import QtWidgets

from ..gui.dialogCreateNewAccount import Ui_dialogCreateNewAccount


class DialogCreateNewAccount(QtWidgets.QDialog, Ui_dialogCreateNewAccount):
    """
    implementation of the dialogCreateNewAccount Gui
    """

    def __init__(self, parent=None):
        super(DialogCreateNewAccount, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # Connect add button with a custom function (addAcc)
        self.buttonAddNewAccount.clicked.connect(self.add_acc)

    def closeEvent(self, event):
        self.parent.dialog_create_new_acc = None

    def add_acc(self):
        acc_name = str(self.inputAccountName.text())
        if acc_name == "":
            # add popup stating the acc name is missing
            return
        balance = self.inputInitialAmount.text()
        if balance == "":
            # add popup stating the initial balance is missing
            return
        balance = int(balance)
        self.parent.database.add_acc(acc_name, balance)

        currentRowCount = self.parent.tableWidgetAccounts.rowCount() + 1
        self.parent.tableWidgetAccounts.setRowCount(currentRowCount)

        item_acc_name = QtWidgets.QTableWidgetItem(acc_name)
        self.parent.tableWidgetAccounts.setItem(currentRowCount - 1, 0, item_acc_name)
        item_balance = QtWidgets.QTableWidgetItem(str(balance))
        self.parent.tableWidgetAccounts.setItem(currentRowCount - 1, 1, item_balance)

        # delete the initial combo box item and add a new one for the account
        if self.parent.comboChooseAccount.currentText() == "NoAccountSaved":
            self.parent.comboChooseAccount.removeItem(int(0))
        self.parent.comboChooseAccount.addItem(acc_name)

        self.parent.buttonAddExpenses.setEnabled(True)
        self.parent.buttonAddIncome.setEnabled(True)
