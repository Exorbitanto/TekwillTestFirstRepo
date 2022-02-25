import json
from my_library.numeric_tools import get_int_input

file_name = "ex_5_dishes.json"

def get_list_from_json_file(file_name):
    try:
        file = open(file_name, 'r')
        text = file.read()
        file.close()
        try:
            return json.loads(text)
        except Exception:
            return list()
    except FileNotFoundError:
        file = open(file_name, 'w+')
        file.close()

def list_all_dishes():
    my_list = get_list_from_json_file(file_name)
    if len(my_list) > 0:
        for dish in my_list:
            print(f"{dish}")

def add_dish():
    new_dish = input("Please enter the new dish: ")
    my_list = get_list_from_json_file(file_name)
    my_list.append(new_dish)
    data_to_file = json.dumps(my_list)
    file = open(file_name, 'w')
    file.write(data_to_file)
    file.close()

list_all_dishes()
variant = 0
while variant > 2 or variant<= 0:
    variant = get_int_input("Please choose: (1)List all dishes (2)Add a dish: ")

if variant == 1:
    list_all_dishes()
elif variant == 2:
    add_dish()
