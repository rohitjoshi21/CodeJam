'''
Question 5 

Go to this link for question:-
https://www.hackerearth.com/zh/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/y?
'''

T = int(input())

for _ in range(T):
    N = int(input('\n'))
    m = N % 6
    if m == 0:
        m = 6
    toAdd = 11 - 2 * (m - 1)

    opposite = N + toAdd
    rem = opposite % 3
    print(opposite, end=' ')
    if rem == 1:
        print('WS')
    elif rem == 2:
        print('MS')
    else:
        print('AS')
