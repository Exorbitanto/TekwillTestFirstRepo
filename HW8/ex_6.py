from my_library.string_tools import string_eliminate_punctuation

file = open("ex_2_file.txt","r")
data = file.read()
text = string_eliminate_punctuation(data).split(" ")
print(len(text))