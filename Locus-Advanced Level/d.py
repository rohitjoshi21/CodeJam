'''
Question 4
Reciprocal Cycles
Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler026/problem
'''


def divide(a, b):

    integer = a // b
    remainder = a % b
    seen = {remainder: 0}
    digits = ''
    while True:
        remainder *= 10
        digits += str(remainder // b)
        remainder = remainder % b
        if remainder in seen:
            where = seen[remainder]
            return digits[where:]
        else:
            seen[remainder] = len(digits)


def compute(n):
    largeRec = 0
    largeNum = 1
    for i in range(2, n):
        d = divide(1, i)
        if d == '0':
            continue
        a = len(d)
        if a > largeRec:
            largeRec = a
            largeNum = i
    return largeNum


# print(divide(1, 7))
# # print(divide(1, 3))

t = int(input())

for i in range(t):
    N = int(input())
    print(compute(N))
