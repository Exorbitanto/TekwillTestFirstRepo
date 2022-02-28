import json
from builtins import sorted
from datetime import datetime
from my_library.numeric_tools import *

def print_list_of_values_from_list_of_dicts(my_dict:dict,key_name:str):
    for dict in my_dict:
        print(dict[key_name])

def calculate_total_monthly_salary(my_dict:dict):
    sum = 0
    for dict in my_dict:
        sum = sum + dict["salary"]
    return sum

def calculate_texes_per_month(my_dict:dict, tax_rate:float):
    return calculate_total_monthly_salary(my_dict) * tax_rate / 100

def print_highest_paid_imployees(my_dict:dict, n:int):
    salary_list = list()
    for dict_el in my_dict:
        salary_list.append(dict_el["salary"])
    salary_list = sorted(salary_list, reverse=True)
    index = 0
    for i in range(n):
        for dict_el in my_dict:
            if salary_list[index] == dict_el["salary"]:
                print(f"{dict_el['name']} | {dict_el['position']} | {dict_el['salary']} | {dict_el['employee_from']}")
        index += 1

def print_longest_time_in_company_imployees(my_dict:dict, n:int):
    time_in_company = list()
    for dict_el in my_dict:
        time_in_company.append(datetime.strptime(dict_el["employee_from"],'%m/%d/%Y'))
    time_in_company = sorted(time_in_company)
    index = 0
    for i in range(n):
        for dict_el in my_dict:
            if time_in_company[index] == datetime.strptime(dict_el["employee_from"],'%m/%d/%Y'):
                print(f"{dict_el['name']} | {dict_el['position']} | {dict_el['salary']} | {dict_el['employee_from']}")
        index += 1


file = open("ex_2.json", "r")
data = json.loads(file.read())

print("1: List all employee names")
print("2: List all position names")
print("3: Calculate the amount of salary the company has to pay per month in total")
print("4: Calculate the amount of money the company has to pay in taxes per month. (Tax % Value is input from the console)")
print("5: Display information for the top 10 highest paid employees (name, position, salary, employment_start_date) from highest paid to lower.")
print("6: Display information for the top 10 employees with the longest time in the company (name, position, salary, employment_start_date) from highest to lower.")

option = 0
while option < 1 or option > 6:
    option = get_int_input("Please choose what to do (1-6) :")
    if option == 1:
        print_list_of_values_from_list_of_dicts(data, "name")
    elif option == 2:
        print_list_of_values_from_list_of_dicts(data, "position")
    elif option == 3:
        print(f"Total salary amount: {calculate_total_monthly_salary(data)}")
    elif option == 4:
        tax_rate = get_float_input("Please enter the current salary tax rate (%): ")
        print(calculate_texes_per_month(data, tax_rate))
    elif option == 5:
        print_highest_paid_imployees(data,10)
    elif option == 6:
        print_longest_time_in_company_imployees(data,10)