from my_library.numeric_tools import get_int_input

n=0
while n < 2:
    n = get_int_input("Enter how many fib numbers you need (must be al least 2): ")
    fib_list = [0, 1]
    for i in range(n-len(fib_list)):
        fib_list.append(fib_list[-1]+ fib_list[-2])

print(fib_list)