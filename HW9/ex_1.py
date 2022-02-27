from my_library.numeric_tools import get_int_input

n = get_int_input("Enter how many fib numbers you need: ")
fib_list = [0, 1]
for i in range(n):
    fib_list.append(fib_list[-1]+ fib_list[-2])

print(fib_list)