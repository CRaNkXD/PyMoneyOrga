from ..database.database_interface import DatabaseInterface


def add_income(database: DatabaseInterface, acc_name, amount, description=None):
    """
    adds an income to the specified account in the database
    """
    if description is None:
        description = "income"

    with database.get_session() as session:
        acc = database.get_acc(session, acc_name)
        acc.add_income(amount, description)


def add_expense(database: DatabaseInterface, acc_name, amount, description=None):
    """
    adds an expense to the specified account in the database
    """
    if description is None:
        description = "expense"

    with database.get_session() as session:
        acc = database.get_acc(session, acc_name)
        acc.add_expense(amount, description)


def add_acc(database: DatabaseInterface, acc_name, balance, currency):
    """
    adds a new account to the database
    """
    with database.get_session() as session:
        database.add_acc(session, acc_name, balance, currency)


def delete_acc(database: DatabaseInterface, acc_name):
    """
    adds the specified account from the database
    """
    with database.get_session() as session:
        database.delete_acc(session, acc_name)


def get_all_acc(database: DatabaseInterface):
    """
    returns all accounts which are saved in the database
    if not existent returns an empty list []
    """
    with database.get_session() as session:
        accs = database.get_all_acc(session)
        database.expunge_all(session)

    return accs


def get_acc(database: DatabaseInterface, acc_name):
    """
    returns the specified account from the database
    if not existent returns None
    """
    with database.get_session() as session:
        acc = database.get_acc(session, acc_name)
        database.expunge_all(session)

    return acc


def get_transactions(
    database: DatabaseInterface, acc_name, reverse=False, max_length=-1, offset=0
):
    """
    returns all transactions from the specified account
    if not existent returns an empty list []
    """
    with database.get_session() as session:
        transactions = database.get_transactions(
            session, acc_name, reverse, max_length, offset
        )
        database.expunge_all(session)

    return transactions

def undo_last_transaction(database: DatabaseInterface, acc_name):
    """
    undoes the last transaction from the specified acc if there is one
    """
    with database.get_session() as session:
        acc = database.get_acc(session, acc_name)
        if acc.transactions:
            acc.balance -= acc.transactions[-1].amount
            database.delete_last_transaction(session, acc_name)


def get_currency(database: DatabaseInterface, acc_name):
    """
    returns the currency of the specified account
    """
    with database.get_session() as session:
        acc = database.get_acc(session, acc_name)
        # workaround for call of init_chart when the combo box is cleared and no account name is specified
        if acc is None:
            currency = ""
        else:
            currency = acc.currency

    return currency
