from .account import Account

class Database(object):
    """description of class"""

    def __init__(self, file_name):
        self.file_name = file_name
        self.dict_all_acc = {}

    def __str__(self):
       return f"Database from file {self.file_name} with len(self.dict_all_acc) accounts saved."

    def __repr__(self):
        return f"Database from file {self.file_name} with len(self.dict_all_acc) accounts saved."

    def save_value(self, acc_name, value):
        pass

    def add_acc(self, account):
        self.dict_all_acc[account.acc_name] = account



