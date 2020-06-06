import unittest
from PyMoneyOrga.account import Account

class Test_account(unittest.TestCase):
    def setUp(self):
        self.daniels_account = Account("Daniel",100)
        return super().setUp()

    def test_add_cash_in_euro(self):
        self.daniels_account.add_cash_in_euro(100)
        self.assertEqual(self.daniels_account.cash_in_euro,200)

    def test_acc_name(self):
        self.assertEqual(self.daniels_account.acc_name,"Daniel")

if __name__ == '__main__':
    unittest.main()
