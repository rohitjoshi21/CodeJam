'''
Question 4
Watermelon
https://codeforces.com/problemset/problem/4/A
'''


def solve(w):
    if w % 2 == 0 and w > 2:
        return 'YES'
    else:
        return 'NO'


w = int(input())
print(solve(w))
