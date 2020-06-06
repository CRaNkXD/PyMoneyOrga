
class Account(object):
    """Saves the amount of cash in an account"""

    def __init__(self, acc_name, cash_in_euro):
        self.acc_name = acc_name
        self.cash_in_euro = cash_in_euro
        
    
    def add_cash_in_euro(self, amount_in_euro):
        self.cash_in_euro += amount_in_euro

    def add_expenses_in_euro(self, amount_in_euro):
        self.cash_in_euro -= amount_in_euro
        print(self.cash_in_euro)
    
    @property
    def cash_in_euro(self):
        return self.cash_in_euro
    
    @property
    def acc_name(self):
        return self.acc_name
