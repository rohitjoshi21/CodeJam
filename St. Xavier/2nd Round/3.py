'''
Question 3
Print collatz sequence of an input number.
(You can get detail about collatz sequence from this site:
https://en.wikipedia.org/wiki/Collatz_conjecture)
'''

def getCollatz(n):
    if n <= 0:
        return []
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


n = int(input())

print(getCollatz(n))
