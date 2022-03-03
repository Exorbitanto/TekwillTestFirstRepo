from NumberList import NumberList

my_NumberList = NumberList([10, 22, 58, 104.23, 25.5, 24.8, 99.99])
print(my_NumberList)
my_NumberList.append(2022)
print(my_NumberList)
my_NumberList.extend([3022,4022])
print(my_NumberList)

print(my_NumberList.get_sum())
print(my_NumberList.get_average())