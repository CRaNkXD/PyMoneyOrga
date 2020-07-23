import unittest
from PyMoneyOrga.domain.money import Money


class TestMoney(unittest.TestCase):
    def setUp(self):
        self.money = Money(100, "EUR")
        return super().setUp()

    def test_add(self):
        money = self.money + Money(100, "EUR")
        self.assertEqual(money.amount, 200)

    def test_convert(self):
        money_usd = Money.convert_to(self.money, "USD")
        self.assertEqual(money_usd.amount, 100 * Money.VALID_CURRENCIES["USD"])
        self.assertEqual(money_usd.currency, "USD")


if __name__ == "__main__":
    unittest.main()
