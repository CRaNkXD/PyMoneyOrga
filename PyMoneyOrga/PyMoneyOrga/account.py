
class Account(object):
    """Saves the amount of cash in an account"""

    def __init__(self, sAccName, iCash):
        self.sAccName = sAccName
        self.iCash = iCash
        
    
    def addCash(self, iAmount):
        self.iCash += iAmount

    def addExpenses(self, iAmount):
        self.iCash -= iAmount
        print(self.iCash)

    def getCash(self):
        return self.iCash

    def getName(self):
        return self.sAccName
