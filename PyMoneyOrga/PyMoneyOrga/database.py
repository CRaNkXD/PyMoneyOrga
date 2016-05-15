from .account import Account

class Database(object):
    """description of class"""

    def __init__(self, sFileName):
        self.sFileName = sFileName
        self.acAllAccs = {}


    def save_value(self, sAccName, iValue):
        pass

    def addAcc(self, Account):
        self.acAllAccs[Account.sAccName] = Account



