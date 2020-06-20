from .database.database_sqlite import Database_sqlite


class Account(object):
    """ Combines a name with a balance value """

    def __init__(self, acc_name, balance):
        self._acc_name = acc_name
        self._balance = balance


    def __str__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._balance} €"
        

    def __repr__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._balance} €"


    def add_income(self, amount):
        self._balance += amount


    def add_expenses(self, amount):
        self._balance -= amount

    

    @property
    def balance(self):
        return self._balance

    
    @property
    def acc_name(self):
        return self._acc_name