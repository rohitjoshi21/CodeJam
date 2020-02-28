'''
Question 3
Take a integer input N and print two primes just below and above it.
'''

def isPrime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def main():
    n = int(input())
    a = 2
    lastPrime = 2
    while True:
        if isPrime(a):
            newLastPrime = a

        a += 1
        if newLastPrime > n:
            print('The prime number before %d is %d' % (n, lastPrime))
            print('The prime number after %d is %d' % (n, newLastPrime))
            break
        lastPrime = newLastPrime


main()
