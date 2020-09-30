import unittest
from PyMoneyOrga.service_layer import services_account
from PyMoneyOrga.database.database_sqlite import DatabaseSqlite


class TestServicesAccount(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseSqlite(url="sqlite:///pymoneyorga.sqlite.test")
        self.acc_name_1 = "User1"
        return super().setUp()

    def test_add_acc(self):
        services_account.add_acc(self.database, self.acc_name_1, 100, "EUR")
        with self.database.get_session() as session:
            acc = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc.acc_name, self.acc_name_1)
            self.assertEqual(acc.balance, 100)

    def test_add_income_updates_balance(self):
        services_account.add_acc(self.database, self.acc_name_1, 100, "EUR")
        services_account.add_income(self.database, self.acc_name_1, 100)
        with self.database.get_session() as session:
            acc = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc.balance, 200)

    def test_add_income_adds_transaction(self):
        services_account.add_acc(self.database, self.acc_name_1, 100, "EUR")
        services_account.add_income(self.database, self.acc_name_1, 100)
        with self.database.get_session() as session:
            acc = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc.transactions[0].new_balance, 200)
            self.assertEqual(acc.transactions[0].amount, 100)
            self.assertEqual(acc.transactions[0].description, "income")

    def test_add_expense_updates_balance(self):
        services_account.add_acc(self.database, self.acc_name_1, 200, "EUR")
        services_account.add_expense(self.database, self.acc_name_1, 50)
        with self.database.get_session() as session:
            acc = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc.balance, 150)

    def test_add_expense_adds_transaction(self):
        services_account.add_acc(self.database, self.acc_name_1, 200, "EUR")
        services_account.add_expense(self.database, self.acc_name_1, 50)
        with self.database.get_session() as session:
            acc = self.database.get_acc(session, self.acc_name_1)
            self.assertEqual(acc.transactions[0].new_balance, 150)
            self.assertEqual(acc.transactions[0].amount, -50)
            self.assertEqual(acc.transactions[0].description, "expense")

    def tearDown(self):
        self.database._clear_all_tables()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
