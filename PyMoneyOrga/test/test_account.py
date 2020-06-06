import unittest
from PyMoneyOrga.account import Account

class Test_account(unittest.TestCase):
    def setUp(self):
        self.daniels_account = Account("Daniel",100)
        return super().setUp()

    def test_addCash(self):
        self.daniels_account.addCash(100)
        self.assertEqual()
if __name__ == '__main__':
    unittest.main()
