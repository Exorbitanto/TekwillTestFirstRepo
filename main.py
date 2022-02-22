def ex_1():
    user_input = input("Please enter a word phrase, or sequence to check if it is a palindrome or not: ").lower().replace(" ","")
    reverse_input = user_input[len(user_input)::-1]
    return True if user_input == reverse_input else False

def ex_2():
    pass


if __name__ == '__main__':
    # We can store the functions as values in a dict
    exercises_map = {
        1: ex_1,
        2: ex_2
    }
    print('Type the number of the exercise to test:')
    print('1: Palindrome exercise')
    print('2: Prime number exercise')
    ex_nr = int(input('Exercise number: '))
    print(exercises_map[ex_nr]())  # Executing the function at the selected number