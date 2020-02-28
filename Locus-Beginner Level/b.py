'''
Question 2
Winning Lottery Ticket
Link: https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/winning-lottery-ticket
'''

n = int(input())
p = [input().strip() for _ in range(n)]

full = 2**10 - 1
count = [0 for _ in range(full + 1)]

for s in p:
    zz = 0
    for c in s:
        zz |= 1 << (ord(c) - ord('0'))
    count[zz] += 1

res = 0
for i in range(full + 1):
    for j in range(i + 1, full + 1):
        if i | j == full:
            res += count[i] * count[j]

res += count[full] * (count[full] - 1) / 2
print(int(res))
