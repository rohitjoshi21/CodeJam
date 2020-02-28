'''
Question 7
Take a integer input N and find the pythagorean triplets such that a+b+c = N
Example:
Input: 12
Output: 3 4 5

Explanation: 3+4+5 = 12 and 3^2+4^2=5^2
'''

import math


def checkTriplets(total):

    upperLimit = int(total / 2)

    for a in range(2, upperLimit):
        for b in range(2, upperLimit):
            if a + b > upperLimit:
                c = total - a - b
                if a**2 + b**2 == c**2:
                    return (a, b, c)


def main():
    n = int(input('Enter a number? '))
    print(checkTriplets(n))


# Main Execution
main()
