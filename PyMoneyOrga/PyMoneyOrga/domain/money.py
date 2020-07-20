class Money(object):
    """Class for representing money in the desired currency"""
    # The base currency is euro
    _VALID_CURRENCIES = {"EUR":1.0, "USD":1.14}

    def __init__(self, amount, currency="EUR"):
        if currency not in Money._VALID_CURRENCIES:
            print(f"The currency {currency} is not valid or not implemented!")
        self._amount = amount
        self._currency = currency

    def __repr__(self):
        return f"{self._amount} {self._currency}"

    def __str__(self):
        return f"{self._amount} {self._currency}"

    def __add__(self, money):
        if self._currency != money.currency:
            print(f"Cannot add money when the currency does not match ({self._currency} != {money.currency}")
        amount = self._amount + money.amount
        return Money(amount, self._currency) 

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    @classmethod
    def convert_to(money: Money, new_currency):
        if new_currency not in Money._VALID_CURRENCIES:
            print(f"The currency {new_currency} is not valid or not implemented!")
        euro = money.amount / Money._VALID_CURRENCIES[money.currency]
        return Money(euro * Money._VALID_CURRENCIES[new_currency], new_currency)
