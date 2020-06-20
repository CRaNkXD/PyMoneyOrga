import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from ..gui.dialogDeleteAccount import Ui_dialogDeleteAccount



class DialogDeleteAccount(QtWidgets.QDialog, Ui_dialogDeleteAccount):
    """implementation of the dialogCreateNewAccount Gui"""
    
    def __init__(self, parent=None):
        super(DialogDeleteAccount, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # Connect add button with a custom function 
        self.buttonDeleteAccount.clicked.connect(self.delete_acc)
        self.buttonCancel.clicked.connect(self.close)

        # delete the initial combo box item and copy the items from the main window
        if self.parent.comboChooseAccount.count() > 1 or self.parent.comboChooseAccount.currentText() != "NoAccountSaved":
            self.comboChooseAccount.removeItem(0)
            for i in range(self.parent.comboChooseAccount.count()):
                text = self.parent.comboChooseAccount.itemText(i)
                self.comboChooseAccount.addItem(text)


    def closeEvent(self, event):
        self.parent.dialog_delete_acc = None


    def delete_acc(self):
        acc_name = self.comboChooseAccount.currentText()
        if acc_name == "NoAccountSaved":
            # add open an popup stating there are no accounts to delete
            return
        self.parent.database.delete_account_table(acc_name)
        self.parent.init_gui_with_database()
        for i in range(self.comboChooseAccount.count()):
            if self.comboChooseAccount.itemText(i) == acc_name:
                self.comboChooseAccount.removeItem(i)

        if self.comboChooseAccount.count() == 0:
            self.comboChooseAccount.addItem("NoAccountSaved")
