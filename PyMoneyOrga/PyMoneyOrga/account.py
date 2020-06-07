
class Account(object):
    """Saves the amount of cash in an account"""

    def __init__(self, acc_name, cash_in_euro):
        self._acc_name = acc_name
        self._cash_in_euro = cash_in_euro

    def __str__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._cash_in_euro}"
        
    def __repr__(self):
        return f"Account Name: {self._acc_name}; Money in Account: {self._cash_in_euro}"

    def add_cash_in_euro(self, amount_in_euro):
        self._cash_in_euro += amount_in_euro

    def add_expenses_in_euro(self, amount_in_euro):
        self._cash_in_euro -= amount_in_euro
        print(self._cash_in_euro)
    
    def _get_cash_in_euro(self):
        return self._cash_in_euro
    
    cash_in_euro = property(_get_cash_in_euro)
    
    def _get_acc_name(self):
        return self._acc_name

    acc_name = property(_get_acc_name)