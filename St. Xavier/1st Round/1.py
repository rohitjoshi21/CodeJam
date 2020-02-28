'''
Question 1
Check whether an input string is palindrome or not.
'''


def isPalindrome(s):
    reverse = ''
    for i in s[::-1]:
        reverse += i

    if reverse == s:
        return True
    else:
        return False


string = input()

if isPalindrome(string):
    print('True')
else:
    print('False')
