import json

class CurrencyConversionService:


    def __init__(self):
        pass

    @staticmethod
    def object_list():
        from CurrencyConversion import CurrencyConversion
        file = open("conversion_rates.json", "r")
        data = file.read()
        data_list = json.loads(data)
        file.close()

        object_list = list()
        for dict_el in data_list.values():
            object_list.append(CurrencyConversion(dict_el['name'], dict_el['code'], "MDL", dict_el['rate'], dict_el['inverseRate']))
        return CurrencyConversionService._bubblesort_object_list(object_list)

    @staticmethod
    def _bubblesort_object_list(object_list):
        for n in range(len(object_list) - 1, 0, -1):
            for i in range(n):
                if object_list[i] > object_list[i + 1]:
                    object_list[i], object_list[i + 1] = object_list[i + 1], object_list[i]
        return object_list

    @staticmethod
    def list_of_available_currencies():
        my_list = list()
        list_of_objects = CurrencyConversionService.object_list()
        for object in list_of_objects:
            my_list.append(object.currency)
        my_list.append("MDL")
        return my_list

    @staticmethod
    def get_currency_object(currency):
        object_list = CurrencyConversionService.object_list()
        for i in object_list:
            if currency == i.currency_from:
                return i

    @staticmethod
    def convert(currency_from, currency_to, desired_amount):
        currency_from_object = CurrencyConversionService.get_currency_object(currency_from)
        currency_to_object = CurrencyConversionService.get_currency_object(currency_to)
        if currency_to == "MDL":
            my_object = CurrencyConversionService.get_currency_object(currency_from)
            return desired_amount * currency_from_object.inverse_rate
        elif currency_from == "MDL":
            my_object = CurrencyConversionService.get_currency_object(currency_to)
            return desired_amount * currency_to_object.conversion_rate
        else:
            return desired_amount * currency_from_object.inverse_rate / currency_to_object.inverse_rate