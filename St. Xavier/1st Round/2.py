'''
Question 1
Find all the real roots of a quadratic equation.
'''

a, b, c = map(int, input().split())

# Determinant
D = b**2 - 4 * a * c

if D > 0:
    root1 = (-b + D**(1 / 2)) / (2 * a)
    root2 = (-b - D**(1 / 2)) / (2 * a)
    print(root1, root2)
elif D == 0:
    root1 = -b / (2 * a)
    print(root1, root1)
else:
    print('No real roots')
