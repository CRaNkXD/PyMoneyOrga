from PySide2 import QtWidgets

from ..service_layer import services_account, services_gui
from ..gui.UIdialogCreateNewAccount import Ui_dialogCreateNewAccount


class DialogCreateNewAccount(QtWidgets.QDialog, Ui_dialogCreateNewAccount):
    """
    implementation of the dialogCreateNewAccount Gui
    """

    def __init__(self, parent=None):
        super(DialogCreateNewAccount, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.comboCurrency.addItems(services_gui.valid_currencies())
        # Connect add button with a custom function (addAcc)
        self.buttonAddNewAccount.clicked.connect(self.add_acc)

    def closeEvent(self, event):
        """
        sets the variable containing the dialog to None if the dialog is closed
        this allows the dialog to be opened again
        """
        self.parent.dialog_create_new_acc = None

    def add_acc(self):
        """
        adds an account to the database
        acc_name is specified by inputAccountName
        balance is specified by inputInitialAmount
        """
        acc_name = str(self.inputAccountName.text())
        info_list = []
        if acc_name == "":
            info_list.append("Account name is not specified!")

        balance = self.inputInitialBalance.text()
        if balance == "":
            info_list.append("Initial balance is not specified!")

        if info_list != []:
            info_msg = ""
            for msg in info_list:
                info_msg += msg + "\n"
            services_gui.show_info_msg_box(info_msg)
            return

        balance = int(balance)
        services_account.add_acc(self.parent.database, acc_name, balance)

        accs = services_account.get_all_acc(self.parent.database)
        self.parent.init_comboChooseAccount(accs)
        self.parent.init_table_accounts(accs)
        self.parent.enable_buttons(True)
