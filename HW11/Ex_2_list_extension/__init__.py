from NumberList import NumberList

my_NumberList = NumberList([10, 22, 58, 104.23, 25.5, 24.8, 99.99])
print(my_NumberList)
my_NumberList.append(2022)
print(my_NumberList)
my_NumberList.extend([3022,4022])
print(my_NumberList)

print(f"The sum is: {my_NumberList.get_sum()}")
print(f"The average is: {my_NumberList.get_average()}")