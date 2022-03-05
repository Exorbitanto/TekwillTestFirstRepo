import json


class CurrencyConversion:

    def __init__(self, name, currency_from, currency_to, conversion_rate, inverse_rate):
        self._name = name
        self._currency_from = currency_from
        self._currency_to = currency_to
        self._conversion_rate = conversion_rate
        self._inverse_rate = inverse_rate

    def __str__(self):
        return f"{self._name}: {self._inverse_rate:.4f} MDL for 1 {self._currency_from} or {self._conversion_rate:.4f} {self._currency_from} for 1 MDL"

    @staticmethod
    def object_list():
        file = open("conversion_rates.json", "r")
        data = file.read()
        data_list = json.loads(data)
        file.close()

        object_list = list()
        for dict_el in data_list.values():
            object_list.append(CurrencyConversion(dict_el['name'], dict_el['code'], "MDL", dict_el['rate'], dict_el['inverseRate']))
        return CurrencyConversion._bubblesort_object_list(object_list)

    @staticmethod
    def _bubblesort_object_list(object_list):
        for n in range(len(object_list) - 1, 0, -1):
            for i in range(n):
                if object_list[i] > object_list[i + 1]:
                    object_list[i], object_list[i + 1] = object_list[i + 1], object_list[i]
        return object_list

    @property
    def currency(self):
        return self._currency_from

    @property
    def inverse_rate(self):
        return self._inverse_rate

    @staticmethod
    def list_of_available_currencies():
        my_list = list()
        list_of_objects = CurrencyConversion.object_list()
        for object in list_of_objects:
            my_list.append(object.currency)
        my_list.append("MDL")
        return my_list

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

