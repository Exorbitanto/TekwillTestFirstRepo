import string

def string_reversed(text: str):
    return text[::-1]

def string_to_words_set(text:str):
    return set(string_eliminate_punctuation(text).split(" "))

def string_eliminate_punctuation(text:str):
    punctuation_marks = string.punctuation
    punctuation_list = list()
    for letter in punctuation_marks:
        punctuation_list.append(letter)
    punctuation_list.append("\n")
    for punctuation_mark in punctuation_list:
        text = text.replace(punctuation_mark," ")
    text = text.replace("  "," ")
    text = text.strip()
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
