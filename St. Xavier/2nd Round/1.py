vowels = ['a', 'e', 'i', 'o', 'u']

vowelC = 0
consoC = 0
digitC = 0
whiteC = 0
symbolC = 0


string = input()

for i in string:
    if i.isalpha():
        if i.lower() in vowels:
            vowelC += 1
        else:
            consoC += 1
    elif i.isdigit():
        digitC += 1
    elif i.isspace():
        whiteC += 1
    else:
        symbolC += 1

print('\nNo of Vowels = ', vowelC)
print('No of Consonant = ', consoC)
print('No of Digit = ', digitC)
print('No of Whitespace = ', whiteC)
print('No of Symbols = ', symbolC)
