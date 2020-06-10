
class Account(object):
    """Saves the amount of cash in an account"""

    def __init__(self, acc_name, balance):
        self._acc_name = acc_name
        self._balance = balance


    def __str__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._balance} €"
        

    def __repr__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._balance} €"


    def add_cash(self, amount_in_euro):
        self._balance += amount_in_euro


    def add_expenses(self, amount_in_euro):
        self._balance -= amount_in_euro
        print(self._balance)
    

    @property
    def balance(self):
        return self._balance

    
    @property
    def acc_name(self):
        return self._acc_name