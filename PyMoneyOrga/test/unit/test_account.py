import unittest
from PyMoneyOrga.domain.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.user_account = Account("User", 100, "EUR")
        return super().setUp()

    def test_add_income(self):
        self.user_account.add_income(100, "income")
        self.assertEqual(self.user_account.balance, 200)

    def test_add_expense(self):
        self.user_account.add_expense(50, "expense")
        self.assertEqual(self.user_account.balance, 50)

    def test_acc_name(self):
        self.assertEqual(self.user_account.acc_name, "User")


if __name__ == "__main__":
    unittest.main()
