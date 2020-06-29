class Database(object):
    """description of class"""

    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f"Database from file {self.file_name}."

    def __repr__(self):
        return f"Database from file {self.file_name}."

    def save_value(self, acc_name, value):
        pass

    def add_acc(self, account):
        self.dict_all_acc[account.acc_name] = account
