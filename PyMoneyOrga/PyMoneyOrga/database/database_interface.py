from abc import ABC, abstractmethod

class Database_interface(ABC):
    """description of class"""

    def __init__(self, file_name):
        self.file_name = file_name
    
    
    @abstractmethod
    def add_acc(self, acc_name, balance):
        """add an account to the the account table and commit to database"""
        pass


    @abstractmethod
    def get_acc(self, acc_name):
        """get an account from the database"""
        pass


    @abstractmethod
    def update_acc_balance(self, acc_name, new_balance):
        """get an account from the database"""
        pass


    @abstractmethod
    def add_transaction(self, acc_name, amount, new_balance):
        """add a transaction to the the transaction table and commit to database"""
        pass



