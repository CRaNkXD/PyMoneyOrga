import unittest
from PyMoneyOrga.domain.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.user_account = Account("User", 100)
        return super().setUp()

    def test_add_cash(self):
        self.user_account.add_income(100)
        self.assertEqual(self.user_account.balance, 200)

    def test_add_expenses(self):
        self.user_account.add_expenses(50)
        self.assertEqual(self.user_account.balance, 50)

    def test_acc_name(self):
        self.assertEqual(self.user_account.acc_name, "User")

    def test_add_expenses_default_description(self):
        self.user_account.add_expenses(50)
        self.assertEqual(self.user_account.transactions[0].description, "expense")


if __name__ == "__main__":
    unittest.main()
