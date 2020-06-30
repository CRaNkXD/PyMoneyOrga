import unittest
from PyMoneyOrga.database.database_sqlite import Database_sqlite


class Test_database_sqlite(unittest.TestCase):
    def setUp(self):
        self.database = Database_sqlite(url="sqlite:///pymoneyorga.sqlite.test")
        return super().setUp()

    def test_add_acc_first(self):
        """
        tests if an account can be set by checking table columns
        """
        self.database.add_acc("Daniel", 100)
        acc = self.database.get_acc("Daniel")
        self.assertEqual(acc["Daniel"], 100)

    def test_add_acc_second(self):
        """
        tests if a second account can be set by checking table
        columns of the first and the second entry
        """
        self.database.add_acc("Daniel", 100)
        self.database.add_acc("Sabine", 200)
        acc_sabine = self.database.get_acc("Sabine")
        acc_daniel = self.database.get_acc("Daniel")
        self.assertEqual(acc_sabine["Sabine"], 200)
        self.assertEqual(acc_daniel["Daniel"], 100)

    def test_get_acc_none(self):
        """
        tests if get acc returns a dict {acc_name: None} if the
        specified account does not exist
        """
        acc = self.database.get_acc("Daniel")
        self.assertEqual(acc["Daniel"], None)

    def test_get_transactions_none(self):
        """
        tests if get transactions returns an empty list [] if the
        specified account does have no transactions
        """
        self.database.add_acc("Daniel", 100)
        transactions = self.database.get_all_transaction("Daniel")
        self.assertEqual(transactions, [])

    def test_add_transactions_first(self):
        """
        tests if a second transaction can be set by checking table
        columns of the first entry
        """
        self.database.add_acc("Daniel", 100)
        self.database.add_transaction("Daniel", 100, 50,"New Car")
        transactions = self.database.get_all_transaction("Daniel")
        self.assertEqual(transactions[0].amount, 100)
        self.assertEqual(transactions[0].new_balance, 50)
        print(transactions[0].time_stamp)

    def test_add_transactions_second(self):
        """
        tests if a second transaction can be set by checking table
        columns of the first and the second entry
        """
        self.database.add_acc("Daniel", 100)
        self.database.add_transaction("Daniel", 100, 50,"New Car")
        self.database.add_transaction("Daniel", 200, 100,"New Laptop")
        transactions = self.database.get_all_transaction("Daniel")
        self.assertEqual(transactions[0].amount, 100)
        self.assertEqual(transactions[0].new_balance, 50)
        self.assertEqual(transactions[1].amount, 200)
        self.assertEqual(transactions[1].new_balance, 100)

    def tearDown(self):
        self.database._clear_all_tables()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
