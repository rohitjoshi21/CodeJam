'''
Question 8
Find all the factors of an input number.
'''


def Factors(n):
    if n <= 0:
        return []
    fac = {1, n}
    upperlimit = int(n**(1 / 2)) + 1

    for i in range(2, upperlimit):
        if n % i == 0:
            fac.add(i)
            a = n // i
            if i != a:
                fac.add(a)
    return sorted(fac)


N = int(input())
print(Factors(N))
