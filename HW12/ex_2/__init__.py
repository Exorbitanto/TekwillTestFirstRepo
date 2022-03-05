from CurrencyConversion import CurrencyConversion
from CurrencyConversionService import CurrencyConversionService

print("Available conversion rates:")
object_list = CurrencyConversion.object_list()
for rate in object_list:
    print(rate)

currency_to = ""
desired_amount = 0

while desired_amount <= 0:
    try:
        desired_amount = float(input("Please enter the amount you want to convert: "))
    except TypeError:
        print("Please enter a float or an integer.")

while currency_to not in CurrencyConversion.list_of_available_currencies():
    currency_to = input("Please enter the currency that you want to convert to MDL:")
    if currency_to == " MDL":
        new_currecncy = ""
        while currency_to not in CurrencyConversion.list_of_available_currencies():
            new_currency = input("Please enter the currency you want to convert from MDL:")
    else:
        CurrencyConversionService.convert_to_MDL(currency_to, desired_amount)