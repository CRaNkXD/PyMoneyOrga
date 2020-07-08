import unittest
from PyMoneyOrga.service_layer import services_gui
from PyMoneyOrga.service_layer import services_account
from PyMoneyOrga.database.database_sqlite import DatabaseSqlite

class TestServicesAccount(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseSqlite(url="sqlite:///pymoneyorga.sqlite.test")
        self.acc_name_1 = "User1"
        self.acc_name_2 = "User2"
        return super().setUp()

    def test_get_all_acc_names(self):
        services_account.add_acc(self.database, self.acc_name_1, 100)
        services_account.add_acc(self.database, self.acc_name_2, 200)
        acc_names = services_gui.get_all_acc_names(self.database)
        self.assertEqual(acc_names, [self.acc_name_1, self.acc_name_2])

    def tearDown(self):
        self.database._clear_all_tables()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
