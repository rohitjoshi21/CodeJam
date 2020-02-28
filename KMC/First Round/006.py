'''
Question 6
Take an input string and remove all the spaces from it.
For eg:
Input: Hello, My name is Rohit
Output: Hello,MynameisRohit
'''
def main():
    string = input('Enter a string? ')

    s = string.replace(' ','')
    print(s)

main()
