'''
Question 2
Check whether an input string is armstrong or not
'''


def checkArmstrong(n, l):
    m = n
    arm = 0
    while m != 0:
        r = m % 10
        arm = arm + r**l
        m = m // 10  # Integer Division

    if arm == n:
        return True
    else:
        return False


def main():
    length = int(input('Enter no. of digits? '))
    n = int(input('Enter a number to check? '))

    a = checkArmstrong(n, length)
    print(a)


main()
