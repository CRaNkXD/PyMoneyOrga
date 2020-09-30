import unittest
import time
from timeit import default_timer as timer
import timeit
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
        with self.database.get_session() as session:
            self.database.add_acc(session, self.acc_name_1, 100, "EUR")
            self.database.commit(session)
            acc = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc.balance, 100)

    def test_add_acc_second(self):
        """
        tests if a second account can be set by checking table
        columns of the first and the second entry
        """
        with self.database.get_session() as session:
            self.database.add_acc(session, self.acc_name_1, 100, "EUR")
            self.database.add_acc(session, self.acc_name_2, 200, "EUR")
            self.database.commit(session)
            acc_user2 = self.database.get_acc(session, self.acc_name_2)
            acc_user1 = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc_user2.balance, 200)
            self.assertEqual(acc_user1.balance, 100)

    def test_get_acc_none(self):
        """
        tests if get acc returns None if the
        specified account does not exist
        """
        with self.database.get_session() as session:
            acc = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc, None)

    def test_get_transactions(self):
        """
        tests if get_transactions returns the
        specified transactions in the right order with the specified amount
        """
        with self.database.get_session() as session:
            self.database.add_acc(session, self.acc_name_1, 100, "EUR")
            self.database.commit(session)
            acc = self.database.get_acc(session, self.acc_name_1)
            acc.add_income(100, "income1")
            time.sleep(0.001)
            acc.add_income(100, "income2")
            time.sleep(0.001)
            acc.add_income(100, "income3")

            transactions = self.database.get_transactions(
                session, self.acc_name_1, False, 2
            )
            self.assertEqual(transactions[0].new_balance, 200)
            self.assertEqual(len(transactions), 2)

            transactions = self.database.get_transactions(
                session, self.acc_name_1, True, 50
            )
            self.assertEqual(transactions[0].new_balance, 400)
            self.assertEqual(len(transactions), 3)

            transactions = self.database.get_transactions(
                session, self.acc_name_1, False, 2, 1
            )
            self.assertEqual(transactions[0].new_balance, 300)

    def tearDown(self):
        self.database._clear_all_tables()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
