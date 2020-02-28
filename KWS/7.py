'''
Question 7

Go to this link for question:-
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/bricks-game-5140869d/
'''

N = int(input())

turn = 1
rounds = 1
while True:
    if turn == 1:
        remove = rounds
        turn = 2

    else:
        remove = rounds * 2
        turn = 1

    if turn == 1:
        rounds += 1

    if N > 0:
        N -= remove

    else:
        break

if turn == 1:
    print('Patlu')
else:
    print('Motu')
