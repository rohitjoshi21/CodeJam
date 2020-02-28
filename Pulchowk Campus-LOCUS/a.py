'''
Question 1
Make them Odd
Link: https://codeforces.com/problemset/problem/1277/B
'''


def getFactor(n):
    powerOfTwo = 0
    while n % 2 == 0:
        n = n // 2
        powerOfTwo += 1

    return (n, powerOfTwo)


def compute(array):
    factors = {}
    for i in array:
        a, b = getFactor(i)
        if a in factors:
            factors[a] = max(factors[a], b)
        else:
            factors[a] = b

    return sum(factors.values())


test = int(input())

for t in range(test):
    n = int(input())
    array = set(map(int, input().split()))
    print(compute(array))
