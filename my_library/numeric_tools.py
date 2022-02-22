def number_isprime(number: float):
    for n in range(2, int(number ** 1 / 2) + 1):
        if number % n == 0:
            return False
    return True

def number_is_perfect(number: int):
    sum1 = 0
    for i in range(1, number):
        if (number % i == 0):
            sum1 = sum1 + i
    return True if (sum1 == number) else False