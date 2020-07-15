from PySide2 import QtWidgets

from ..service_layer import services_account, services_gui
from ..gui.UIdialogDeleteAccount import Ui_dialogDeleteAccount


class DialogDeleteAccount(QtWidgets.QDialog, Ui_dialogDeleteAccount):
    """
    implementation of the dialogCreateNewAccount Gui
    """

    def __init__(self, parent=None):
        super(DialogDeleteAccount, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # connect the buttons with the methods
        self.buttonDeleteAccount.clicked.connect(self.delete_acc)
        self.buttonCancel.clicked.connect(self.close)

        # delete the initial combo box item and copy the items from the main window
        if (
            self.parent.comboChooseAccount.count() > 1
            or self.parent.comboChooseAccount.currentText() != "NoAccountSaved"
        ):
            self.comboChooseAccount.removeItem(0)
            for i in range(self.parent.comboChooseAccount.count()):
                text = self.parent.comboChooseAccount.itemText(i)
                self.comboChooseAccount.addItem(text)

    def closeEvent(self, event):
        """
        sets the variable containing the dialog to None if the dialog is closed
        this allows the dialog to be opened again
        """
        self.parent.dialog_delete_acc = None

    def delete_acc(self):
        acc_name = self.comboChooseAccount.currentText()
        if acc_name == "NoAccountSaved":
            services_gui.show_info_msg_box("There are no accounts to delete!")
            return

        services_account.delete_acc(self.parent.database, acc_name)
        self.parent.init_gui_with_database()
        for i in range(self.comboChooseAccount.count()):
            if self.comboChooseAccount.itemText(i) == acc_name:
                self.comboChooseAccount.removeItem(i)

        if self.comboChooseAccount.count() == 0:
            self.comboChooseAccount.addItem("NoAccountSaved")
            self.parent.enable_buttons(False)
