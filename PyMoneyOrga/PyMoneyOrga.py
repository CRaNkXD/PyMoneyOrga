import sys
from PyMoneyOrga.database.database_sqlite import DatabaseSqlite
from PySide2 import QtWidgets
from PyMoneyOrga.main_window import MainWindow


if __name__ == "__main__":
    database = DatabaseSqlite(url="sqlite:///pymoneyorga.sqlite")
    app = QtWidgets.QApplication(sys.argv)

    prog = MainWindow(database)

    prog.show()
    app.exec_()
