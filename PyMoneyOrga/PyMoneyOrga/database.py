from .account import Account

class Database(object):
    """description of class"""

    def __init__(self, sFileName):
        self.sFileName = sFileName
        self.acAllAccs = {}


    def saveValue(self, sAccName, iValue):
        pass

    def addAcc(self, Account):
        self.acAllAccs[Account.sAccName] = Account



