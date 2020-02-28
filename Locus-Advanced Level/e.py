'''
Question 5
Theatre Square
Link: https://codeforces.com/problemset/problem/1/A
'''

n, m, a = list(map(int, input().split()))

l = n / a
b = m / a

if l % 1 != 0:
    l = int(l) + 1

if b % 1 != 0:
    b = int(b) + 1

print(int(l * b))
