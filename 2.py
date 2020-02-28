'''
Question 2
How do you check if a given string is a palindrome?
'''

def isPal(s):
    rev = ''
    for i in s[::-1]:
        rev += i
    if rev == s:
        return True
    return False


string = input('Enter the string: ')
print(isPal(string))
