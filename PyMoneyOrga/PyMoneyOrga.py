import sys
from PyMoneyOrga.account import Account
from PyMoneyOrga.database.database import Database
from PyQt5 import QtCore, QtGui, QtWidgets
from PyMoneyOrga.user_interface import UserInterface


if __name__ == '__main__':
    database = Database("pymoneyorga.sqlite")
    app = QtWidgets.QApplication(sys.argv)
    
    prog = UserInterface(database)

    prog.show()
    sys.exit(app.exec_())