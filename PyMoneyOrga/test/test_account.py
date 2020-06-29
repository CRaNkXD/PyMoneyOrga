import unittest
from PyMoneyOrga.account import Account


class Test_account(unittest.TestCase):
    def setUp(self):
        self.daniels_account = Account("Daniel", 100)
        return super().setUp()

    def test_add_cash(self):
        self.daniels_account.add_income(100)
        self.assertEqual(self.daniels_account.balance, 200)

    def test_add_expenses(self):
        self.daniels_account.add_expenses(50)
        self.assertEqual(self.daniels_account.balance, 50)

    def test_acc_name(self):
        self.assertEqual(self.daniels_account.acc_name, "Daniel")


if __name__ == "__main__":
    unittest.main()
