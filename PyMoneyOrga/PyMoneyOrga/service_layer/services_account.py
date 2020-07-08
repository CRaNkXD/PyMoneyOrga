from ..database.database_interface import DatabaseInterface


def add_income(database: DatabaseInterface, acc_name, amount, description=None):
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    acc.add_income(amount, description)
    database.commit(session)
    database.close(session)


def add_expense(database: DatabaseInterface, acc_name, amount, description=None):
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    acc.add_expense(amount, description)
    database.commit(session)
    database.close(session)


def add_acc(database: DatabaseInterface, acc_name, balance):
    session = database.get_session()
    database.add_acc(session, acc_name, balance)
    database.commit(session)
    database.close(session)


def delete_acc(database: DatabaseInterface, acc_name):
    session = database.get_session()
    database.delete_acc(session, acc_name)
    database.commit(session)
    database.close(session)


def get_all_acc(database: DatabaseInterface):
    session = database.get_session()
    accs = database.get_all_acc(session)
    database.close(session)
    return accs


def get_acc(database: DatabaseInterface, acc_name):
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    database.close(session)
    return acc


def get_transactions(database: DatabaseInterface, acc_name):
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    if acc is None:
        return []
    transactions = acc.transactions
    database.close(session)
    return transactions
