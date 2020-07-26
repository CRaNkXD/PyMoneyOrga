from PySide2 import QtWidgets
from ..domain.money import Money


def show_info_msg_box(msg):
    """
    shows an info message box with the given message msg
    """
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Information)
    msg_box.setText("Info")
    msg_box.setInformativeText(msg)
    msg_box.setWindowTitle("Info")
    msg_box.exec_()


def valid_currencies():
    """
    returns a list with possible currencies
    """
    return [currency for currency in Money.VALID_CURRENCIES]
