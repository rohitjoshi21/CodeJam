'''
Question 1
Find the greatest common divisior of two input numbers.
'''

def gcd(a, b):
    hcfval = 1
    while True:
        c = b % a
        if c == 0:
            hcfval = a
            break
        a, b = c, a
    return hcfval


num1, num2 = map(int, input().split())

if num1 <= 0 or num2 <= 0:
    print('Invalid input')
else:
    print(gcd(num1, num2))
