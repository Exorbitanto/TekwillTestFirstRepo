power_2_lambda = lambda el: el ** 2
power_3_lambda = lambda el: el ** 3

original_list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_list = list(map(power_2_lambda, original_list_of_integers))
cubed_list = list(map(power_3_lambda, original_list_of_integers))

print(squared_list)
print(cubed_list)