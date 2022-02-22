import my_library.my_library

def ex_1():
    user_input = input("Please enter a word phrase, or sequence to check if it is a palindrome or not: ").lower().replace(" ","")
    reverse_input = my_library.my_string_library.string_reversed(user_input)
    return True if user_input == reverse_input else False

def ex_2():
    user_input = float(input("Please enter a number to check if it is prime of not: "))
    return my_library.my_library.number_isprime(user_input)

def ex_3():
    user_input = int(input("Please enter a number to check if it is perfect of not: "))
    return my_library.my_library.number_is_perfect(user_input)

def ex_4():
    user_input = input("Please enter a string: ")
    print(f"The word set is: {my_library.my_library.string_to_words_set(user_input)}")
    print(f"The used punctuation marks are: {my_library.my_library.string_punctuation_marks(user_input)}")
    print(f"The most commonly used word: {my_library.my_library.dict_kex_with_max_value(my_library.my_library.string_count_number_of_times_word_is_used(user_input))}")
    print(f"The most commonly used punctuation mark: {my_library.my_library.dict_kex_with_max_value(my_library.my_library.string_count_number_of_times_punctuation_is_used(user_input))}")

if __name__ == '__main__':
    # We can store the functions as values in a dict
    exercises_map = {
        1: ex_1,
        2: ex_2,
        3: ex_3,
        4: ex_4
    }
    print('Type the number of the exercise to test:')
    print('1: Palindrome exercise')
    print('2: Prime number exercise')
    print('3: Perfect number exercise')
    print('4: String information')
    ex_nr = int(input('Exercise number: '))
    if ex_nr != 4:
        print(exercises_map[ex_nr]())  # Executing the function at the selected number
    else:
        exercises_map[ex_nr]()  # Executing the function at the selected number