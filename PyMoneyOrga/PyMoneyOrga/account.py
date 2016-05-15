from PyMoneyOrga.database import Database

class Account(object):
    """Saves the amount of cash in an account"""

    def __init__(self, sAccName, iCash):
        self.sAccName = sAccName
        self.iCash = iCash
        
    
    def add_cash(self, iAmount):
        self.iCash += iAmount

    def get_cash(self):
        return self.iCash

    def get_name(self):
        return self.sAccName
