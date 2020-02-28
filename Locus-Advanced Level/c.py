'''
Question 3
Tetrahedron
Link: https://codeforces.com/problemset/problem/166/E
'''

def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 3
    else:
        return int((3**n - (-1)**(n - 1) * 3) / 4)


n = 50
print(f(n) % 1000000007)
