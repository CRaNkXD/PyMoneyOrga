from dataclasses import dataclass
import datetime


@dataclass
class Transaction(object):
    amount: int
    new_balance: int
    description: str
    time_stamp: datetime.datetime
    account_id: int = None


class Account(object):
    """
    Combines a name with a balance value
    """

    def __init__(self, acc_name, balance, transactions=None):
        if transactions is None:
            transactions = []
        self._acc_name = acc_name
        self._balance = balance
        self._transactions = transactions  # list of Transaction objects

    def __str__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._balance} €"

    def __repr__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._balance} €"

    def add_income(self, amount, description="income"):
        self._balance += amount
        self.transactions.append(
            Transaction(
                amount=amount,
                new_balance=self._balance,
                description=description,
                time_stamp=datetime.datetime.now(),
            )
        )

    def add_expenses(self, amount, description="expense"):
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
