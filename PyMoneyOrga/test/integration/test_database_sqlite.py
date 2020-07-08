import unittest
from PyMoneyOrga.database.database_sqlite import DatabaseSqlite


class TestDatabaseSqlite(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseSqlite(url="sqlite:///pymoneyorga.sqlite.test")
        self.acc_name_1 = "User1"
        self.acc_name_2 = "User2"
        return super().setUp()

    def test_add_acc_first(self):
        """
        tests if an account can be set by checking table columns
        """
        session = self.database.get_session()
        self.database.add_acc(session, self.acc_name_1, 100)
        self.database.commit(session)
        acc = self.database.get_acc(session, self.acc_name_1)
        self.assertEqual(acc.balance, 100)
        self.database.close(session)

    def test_add_acc_second(self):
        """
        tests if a second account can be set by checking table
        columns of the first and the second entry
        """
        session = self.database.get_session()
        self.database.add_acc(session, self.acc_name_1, 100)
        self.database.add_acc(session, self.acc_name_2, 200)
        self.database.commit(session)
        acc_user2 = self.database.get_acc(session, self.acc_name_2)
        acc_user1 = self.database.get_acc(session, self.acc_name_1)
        self.assertEqual(acc_user2.balance, 200)
        self.assertEqual(acc_user1.balance, 100)
        self.database.close(session)

    def test_get_acc_none(self):
        """
        tests if get acc returns None if the
        specified account does not exist
        """
        session = self.database.get_session()
        acc = self.database.get_acc(session, self.acc_name_1)
        self.assertEqual(acc, None)
        self.database.close(session)

    # def test_get_transactions_none(self):
    #    """
    #    tests if get transactions returns an empty list [] if the
    #    specified account does have no transactions
    #    """
    #    self.database.add_acc("Daniel", 100)
    #    transactions = self.database.get_all_transaction("Daniel")
    #    self.assertEqual(transactions, [])

    #def test_add_transactions_first(self):
    #    """
    #    tests if a second transaction can be set by checking table
    #    columns of the first entry
    #    """
    #    session = self.database.get_session()
    #    self.database.add_acc(session, self.acc_name_1, 100)
    #    self.database.add_transaction(session, self.acc_name_1, 100, 50, "New Car")
    #    self.database.commit(session)
    #    acc_user1 = self.database.get_acc(session, self.acc_name_1)
    #    self.assertEqual(acc_user1.transactions[0].amount, 100)
    #    self.assertEqual(acc_user1.transactions[0].new_balance, 50)
    #    self.assertEqual(acc_user1.transactions[0].description, "New Car")
    #    self.database.close(session)

    #def test_add_transactions_second(self):
    #    """
    #    tests if a second transaction can be set by checking table
    #    columns of the first and the second entry
    #    """
    #    session = self.database.get_session()
    #    self.database.add_acc(session, self.acc_name_1, 100)
    #    self.database.add_transaction(session, self.acc_name_1, 100, 50, "New Car")
    #    self.database.add_transaction(session, self.acc_name_1, 200, 100, "New Laptop")
    #    self.database.commit(session)
    #    acc_user1 = self.database.get_acc(session, self.acc_name_1)
    #    self.assertEqual(acc_user1.transactions[0].amount, 100)
    #    self.assertEqual(acc_user1.transactions[0].new_balance, 50)
    #    self.assertEqual(acc_user1.transactions[0].description, "New Car")
    #    self.assertEqual(acc_user1.transactions[1].amount, 200)
    #    self.assertEqual(acc_user1.transactions[1].new_balance, 100)
    #    self.assertEqual(acc_user1.transactions[1].description, "New Laptop")
    #    self.database.close(session)

    def tearDown(self):
        self.database._clear_all_tables()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
