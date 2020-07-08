from ..database.database_interface import DatabaseInterface

def add_income(database : DatabaseInterface, acc_name, amount, description=None):
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    acc.add_income(amount, description)
    database.commit(session)
    database.close(session)

def add_expense(database : DatabaseInterface, acc_name, amount, description=None):
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    acc.add_expense(amount, description)
    database.commit(session)
    database.close(session)

def add_acc(database : DatabaseInterface, acc_name, balance):
    session = database.get_session()
    database.add_acc(session, acc_name, balance)
    database.commit(session)
    database.close(session)