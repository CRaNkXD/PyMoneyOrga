class Money(object):
    """Class for representing money in the desired currency"""

    # The base currency is euro
    VALID_CURRENCIES = {"EUR": 1.0, "USD": 1.14}

    @classmethod
    def convert_to(cls, money: "Money", new_currency):
        if new_currency not in cls.VALID_CURRENCIES:
            print(f"The currency {new_currency} is not valid or not implemented!")
        euro = money.amount // cls.VALID_CURRENCIES[money.currency]
        return cls(euro * cls.VALID_CURRENCIES[new_currency], new_currency)

    def __init__(self, amount, currency="EUR"):
        if currency not in Money.VALID_CURRENCIES:
            print(f"The currency {currency} is not valid or not implemented!")
        self._amount = amount
        self._currency = currency

    def __repr__(self):
        return f"{self._amount} {self._currency}"

    def __str__(self):
        return f"{self._amount} {self._currency}"

    def __int__(self):
        return self._amount

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self._currency != other.currency:
                print(
                    f"Cannot add money when the currency does not match \
                    ({self._currency} != {other.currency}"
                )
            amount = self._amount + other.amount
            return Money(amount, self._currency)
        elif isinstance(other, int):
            amount = self._amount + other
            return Money(amount, self._currency)
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: '{self.__class__}' and '{type(other)}'"
            )

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            if self._currency != other.currency:
                print(
                    f"Cannot add money when the currency does not match \
                    ({self._currency} != {other.currency}"
                )
            self._amount += other.amount
        elif isinstance(other, int):
            self._amount += other
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: '{self.__class__}' and '{type(other)}'"
            )

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self._currency != other.currency:
                print(
                    f"Cannot substract money when the currency does not match \
                    ({self._currency} != {other.currency}"
                )
            amount = self._amount - other.amount
            return Money(amount, self._currency)
        elif isinstance(other, int):
            amount = self._amount - other
            return Money(amount, self._currency)
        else:
            raise TypeError(
                f"unsupported operand type(s) for -: '{self.__class__}' and '{type(other)}'"
            )

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            if self._currency != other.currency:
                print(
                    f"Cannot substract money when the currency does not match \
                    ({self._currency} != {other.currency}"
                )
            self._amount -= other.amount
        elif isinstance(other, int):
            self._amount -= other
        else:
            raise TypeError(
                f"unsupported operand type(s) for -: '{self.__class__}' and '{type(other)}'"
            )

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if self._currency != other.currency:
                print(
                    f"Cannot multiply money when the currency does not match \
                    ({self._currency} != {other.currency}"
                )
            amount = self._amount * other.amount
            return Money(amount, self._currency)
        elif isinstance(other, int):
            amount = self._amount * other
            return Money(amount, self._currency)
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: '{self.__class__}' and '{type(other)}'"
            )

    def __imul__(self, other):
        if isinstance(other, self.__class__):
            if self._currency != other.currency:
                print(
                    f"Cannot multiply money when the currency does not match \
                    ({self._currency} != {other.currency}"
                )
            self._amount *= other.amount
        elif isinstance(other, int):
            self._amount *= other
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: '{self.__class__}' and '{type(other)}'"
            )

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            if self._currency != other.currency:
                print(
                    f"Cannot divide money when the currency does not match \
                    ({self._currency} != {other.currency}"
                )
            amount = self._amount // other.amount
            return Money(amount, self._currency)
        elif isinstance(other, int):
            amount = self._amount // other
            return Money(amount, self._currency)
        else:
            raise TypeError(
                f"unsupported operand type(s) for /: '{self.__class__}' and '{type(other)}'"
            )

    def __idiv__(self, other):
        if isinstance(other, self.__class__):
            if self._currency != other.currency:
                print(
                    f"Cannot divide money when the currency does not match \
                    ({self._currency} != {other.currency}"
                )
            self._amount //= other.amount
        elif isinstance(other, int):
            self._amount //= other
        else:
            raise TypeError(
                f"unsupported operand type(s) for /: '{self.__class__}' and '{type(other)}'"
            )

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency
