from CurrencyConversionService import CurrencyConversionService

class CurrencyConversion:

    def __init__(self, name, currency_from, currency_to, conversion_rate, inverse_rate):
        self._name = name
        self._currency_from = currency_from
        self._currency_to = currency_to
        self._conversion_rate = conversion_rate
        self._inverse_rate = inverse_rate

    def __str__(self):
        return f"{self._name}: {self._inverse_rate:.4f} MDL for 1 {self._currency_from} or {self._conversion_rate:.4f} {self._currency_from} for 1 MDL"

    def __gt__(self, other):
        if self._inverse_rate > other.inverse_rate:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._inverse_rate == other.inverse_rate:
            return True
        else:
            return False

    @property
    def currency(self):
        return self._currency_from

    @property
    def inverse_rate(self):
        return self._inverse_rate

    @property
    def conversion_rate(self):
        return self._conversion_rate

    @property
    def name(self):
        return self._name

    @property
    def currency_from(self):
        return self._currency_from



