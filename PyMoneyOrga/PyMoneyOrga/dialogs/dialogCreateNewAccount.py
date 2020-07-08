from PySide2 import QtWidgets

from ..service_layer import services_account
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
        services_account.add_acc(self.parent.database, acc_name, balance)

        accs = services_account.get_all_acc(self.parent.database)
        self.parent.init_comboChooseAccount(accs)
        self.parent.init_table_accounts(accs)
