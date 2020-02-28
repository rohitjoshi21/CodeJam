'''
Question 6
Shuffle Hashing
https://codeforces.com/problemset/problem/1278/A
'''

from collections import Counter


def check(s, h):
    sLen = len(s)
    if len(h) < sLen:
        return 'NO'

    for i, c in enumerate(h):
        subHash = h[i:i + sLen]
        if Counter(subHash) == Counter(s):
            return 'YES'
    return 'NO'


t = int(input())

for z in range(t):
    pwd = input()
    hsh = input()
    print(check(pwd, hsh))
