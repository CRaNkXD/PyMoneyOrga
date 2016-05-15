import sys
from PyMoneyOrga.account import Account
from PyMoneyOrga.database import Database
from PyQt5 import QtCore, QtGui, QtWidgets
from PyMoneyOrga.user_interface import UserInterface


if __name__ == '__main__':
    cDatabase = Database("sFileName")
    app = QtWidgets.QApplication(sys.argv)
    PyMoneyOrgaGui = QtWidgets.QMainWindow()
    
    prog = UserInterface(PyMoneyOrgaGui,cDatabase)

    PyMoneyOrgaGui.show()
    sys.exit(app.exec_())