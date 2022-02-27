from my_library.string_tools import string_eliminate_punctuation

file = open("ex_8_file.txt","r+")
data = file.read()
lines_list = data.split("\n")
my_dict = dict()
for line in lines_list:
    my_dict[line] = len(string_eliminate_punctuation(line).split(" "))
max_words_in_line = max(my_dict.values())
line_with_max_words = list(my_dict.values()).index(max_words_in_line)
print(lines_list[line_with_max_words])