from ..database.database_interface import DatabaseInterface


def add_income(database: DatabaseInterface, acc_name, amount, description=None):
    """
    adds an income to the specified account in the database
    """
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    acc.add_income(amount, description)
    database.commit(session)
    database.close(session)


def add_expense(database: DatabaseInterface, acc_name, amount, description=None):
    """
    adds an expense to the specified account in the database
    """
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    acc.add_expense(amount, description)
    database.commit(session)
    database.close(session)


def add_acc(database: DatabaseInterface, acc_name, balance):
    """
    adds a new account to the database
    """
    session = database.get_session()
    database.add_acc(session, acc_name, balance)
    database.commit(session)
    database.close(session)


def delete_acc(database: DatabaseInterface, acc_name):
    """
    adds the specified account from the database
    """
    session = database.get_session()
    database.delete_acc(session, acc_name)
    database.commit(session)
    database.close(session)


def get_all_acc(database: DatabaseInterface):
    """
    returns all accounts which are saved in the database
    if not existent returns an empty list []
    """
    session = database.get_session()
    accs = database.get_all_acc(session)
    database.close(session)
    return accs


def get_acc(database: DatabaseInterface, acc_name):
    """
    returns the specified account from the database
    if not existent returns None
    """
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    database.close(session)
    return acc


def get_transactions(database: DatabaseInterface, acc_name):
    """
    returns all transactions from the specified account
    if not existent returns an empty list []
    """
    session = database.get_session()
    acc = database.get_acc(session, acc_name)
    if acc is None:
        return []
    transactions = acc.transactions
    database.close(session)
    return transactions
