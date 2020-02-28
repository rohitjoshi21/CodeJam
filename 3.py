'''
Question 3
Count the number of vowels and consonants in a string.
'''
VOWELS = ['a', 'e', 'i', 'o', 'u']

string = input()

vowels = 0
consonants = 0
for i in string.lower():
    if i.isalpha():
        if i in VOWELS:
            vowels += 1
        else:
            consonants += 1


print('No. of vowels is %d' % vowels)
print('No of consonants is %d' % consonants)
