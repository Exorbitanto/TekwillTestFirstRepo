def string_reversed(text: str):
    return text[::-1]

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

def string_to_words_set(text:str):
    return set(string_eliminate_punctuation(text).split(" "))

def string_eliminate_punctuation(text:str):
    punctuation_marks = [".",",","!","?","-",";",":","'","(",")","[","]"]
    for punctuation_mark in punctuation_marks:
        text.replace(punctuation_mark, "")
    return text

def string_punctuation_marks(text:str):
    punctuation_marks = list()
    for letter in text:
        if not letter.isalnum() and letter != " ":
            punctuation_marks.append(letter)
    return punctuation_marks

def string_count_number_of_times_word_is_used(text:str):
    word_dict = dict()
    word_list = text.split(" ")
    word_set = set(word_list)
    for word in word_set:
        word_dict[word] = word_list.count(word)
    return word_dict

def string_count_number_of_times_punctuation_is_used(text:str):
    punctuation_mark_dict = dict()
    punctuation_marks = string_punctuation_marks(text)
    for punctuation_mark in punctuation_marks:
        punctuation_mark_dict[punctuation_mark] = punctuation_marks.count(punctuation_mark)
    return punctuation_mark_dict

def dict_kex_with_max_value(my_dict:dict):
    values_list = list(my_dict.values())
    keys_list = list(my_dict.keys())
    return keys_list[values_list.index(max(values_list))]