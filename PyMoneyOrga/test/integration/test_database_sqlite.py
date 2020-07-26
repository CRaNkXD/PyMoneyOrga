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
        with self.database.get_session() as session:
            self.database.add_acc(session, self.acc_name_1, 100)
            self.database.commit(session)
            acc = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc.balance, 100)

    def test_add_acc_second(self):
        """
        tests if a second account can be set by checking table
        columns of the first and the second entry
        """
        with self.database.get_session() as session:
            self.database.add_acc(session, self.acc_name_1, 100)
            self.database.add_acc(session, self.acc_name_2, 200)
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

    def tearDown(self):
        self.database._clear_all_tables()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
