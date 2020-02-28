'''
Question 3
To generate a 8-character long alpha numeric password containing uppercase,
lowercase and digits.
'''

import random

def main(passLength):
    smallLetters = []
    for i in range(97, 123):
        smallLetters.append(chr(i))

    capitalLetters = []
    for i in range(65, 91):
        capitalLetters.append(chr(i))

    numbers = []
    for i in range(9):
        numbers.append(str(i))

    totalChr = smallLetters + capitalLetters + numbers

    passCode = []
    for i in range(passLength):
        a = random.choice(totalChr)
        passCode.append(a)

    print(''.join(passCode))

#Main Execution
main(8)
