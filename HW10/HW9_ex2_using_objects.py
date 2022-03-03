file = open("ex_2.json", "r")
data = json.loads(file.read())

print("1: List all employee names")
print("2: List all position names")
print("3: Calculate the amount of salary the company has to pay per month in total")
print("4: Calculate the amount of money the company has to pay in taxes per month. (Tax % Value is input from the console)")
print("5: Display information for the top 10 highest paid employees (name, position, salary, employment_start_date) from highest paid to lower.")
print("6: Display information for the top 10 employees with the longest time in the company (name, position, salary, employment_start_date) from highest to lower.")
print("7: Add an employee.")


option = 0
while option < 1 or option > 7:
    option = get_int_input("Please choose what to do (1-7) :")
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
    elif option == 7:
        add_new_employee(data)