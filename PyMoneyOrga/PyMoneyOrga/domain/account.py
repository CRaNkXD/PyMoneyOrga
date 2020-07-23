from dataclasses import dataclass
import datetime


@dataclass
class Transaction(object):
    """
    Data class for transactions made from and to an account. Used in Account class.
    """
    amount: int
    new_balance: int
    description: str
    time_stamp: datetime.datetime
    account_id: int = None # foreign key to Account


class Account(object):
    """
    Class for defining an account.
    """

    def __init__(self, acc_name, balance, transactions=None):
        if transactions is None:
            transactions = []
        self._acc_name = acc_name
        self._balance = balance
        self._transactions = transactions  # list of Transaction objects

    def __str__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._balance}"

    def __repr__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._balance}"

    def add_income(self, amount, description=None):
        """
        Adds an income to the account which is than saved in the transactions list.
        """
        if description is None:
            description = "income"
        self._balance += amount
        self.transactions.append(
            Transaction(
                amount=amount,
                new_balance=self._balance,
                description=description,
                time_stamp=datetime.datetime.now(),
            )
        )

    def add_expense(self, amount, description=None):
        """
        Adds an expense to the account which is than saved in the transactions list.
        """
        if description is None:
            description = "expense"
        self._balance -= amount
        self.transactions.append(
            Transaction(
                amount=-amount,
                new_balance=self._balance,
                description=description,
                time_stamp=datetime.datetime.now(),
            )
        )

    @property
    def balance(self):
        return self._balance

    @property
    def acc_name(self):
        return self._acc_name

    @property
    def transactions(self):
        return self._transactions
