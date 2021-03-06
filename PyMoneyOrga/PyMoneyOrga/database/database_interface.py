from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    """description of class"""

    @abstractmethod
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def get_session(self):
        """
        returns a session from the sessionmaker
        """
        pass

    @abstractmethod
    def commit(self, session):
        """
        commits the changes done to the session into the db
        """
        pass

    @abstractmethod
    def expunge_all(self, session):
        """
        kepp access to all items after expiring
        """
        pass

    @abstractmethod
    def close(self, session):
        """
        closes the session
        """
        pass

    @abstractmethod
    def rollback(self, session):
        """
        rollback any changes in the session
        """
        pass

    @abstractmethod
    def get_all_acc(self, session):
        """
        returns a list of Account objects of all saved accounts
        from the database
        """
        pass

    @abstractmethod
    def add_acc(self, session, acc_name, balance):
        """
        add an account to the the account table and commit to database
        """
        pass

    @abstractmethod
    def delete_acc(self, session, acc_name):
        """
        add an account to the the account table and commit to database
        """
        pass

    @abstractmethod
    def get_acc(self, session, acc_name):
        """
        returns an Account object from the database.
        if not existing None
        """
        pass

    @abstractmethod
    def delete_last_transaction(self, session, acc_name):
        """
        delete the last transaction from the specified acc
        """
        pass

    @abstractmethod
    def get_transactions(
        self, session, acc_name, reverse=False, max_length=-1, offset=0
    ):
        """
        returns a list of transactions from the specified account.
        max_length specifies the max length of the list.
        reverse specifies if the newest transactions will be listed first.
        if not existing [].
        """
        pass
