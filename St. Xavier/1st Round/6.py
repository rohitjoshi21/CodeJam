'''
Question 6
Print the 15th prime number.
'''


def isPrime(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    return False


n = 0
c = 0
while n < 15:
    c += 1
    if isPrime(c):
        # print(c)
        n += 1

print(c)
