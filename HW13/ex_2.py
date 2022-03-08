orginal_list_of_strings = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palindrome_lambda = lambda el: el == el[::-1]
list_of_palindromes = list()

for string in orginal_list_of_strings:
    if palindrome_lambda(string):
        list_of_palindromes.append(string)

print(list_of_palindromes)