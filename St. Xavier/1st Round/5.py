'''
Question 5
Take a string from input and return it after sorting it alphabetically.
'''


def sortLetter(s):
    return ''.join(sorted(s))  # Easy-Peesy


string = input()
print(sortLetter(string))
