from CurrencyConversion import CurrencyConversion
from CurrencyConversionService import CurrencyConversionService
from my_library.numeric_tools import get_float_input, get_int_input

print("1. List all available conversion rates.")
print("2. List top 10 with the lowest conversion rates.")
print("3. List top 10 with the highest conversion rates.")
print("4. Proceed to conversion.")
action = 0
while action < 1 or action > 4:
    action = get_int_input("Please select action (1-4): ")

object_list = CurrencyConversionService.object_list()
if action == 1:
    for rate in object_list:
        print(rate)
elif action == 2:
    for rate in object_list[0:9]:
        print(rate)
elif action == 3:
    for rate in object_list[-1:-10:-1]:
        print(rate)

currency_to = ""
desired_amount = 0

while desired_amount <= 0:
    desired_amount = get_float_input("Please enter the amount you want to convert: ")

while currency_to not in CurrencyConversionService.list_of_available_currencies():
    currency_to = input("Please enter the currency that you want to convert to MDL:").upper()
    if currency_to == "MDL":
        new_currency = ""
        while new_currency not in CurrencyConversionService.list_of_available_currencies():
            new_currency = input("Please enter the currency you want to convert from MDL:").upper()
        converted_amount = CurrencyConversionService.convert("MDL", new_currency, desired_amount)
        print(f"The converted amount is {converted_amount:.2f} {new_currency}")
    else:
        converted_amount = CurrencyConversionService.convert(currency_to, "MDL", desired_amount)
        print(f"The converted amount is {converted_amount:.2f} MDL")

