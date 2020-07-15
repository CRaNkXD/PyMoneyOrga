from PySide2 import QtWidgets

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
