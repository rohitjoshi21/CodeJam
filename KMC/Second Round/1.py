'''
Question 1
Simulate the game scissor, paper and rock
'''

import random


def main():
    print('\nCheck you Luck\n')
    print('Scissor:-  s\nPaper:- p\nRock:- r')

    user = input('Enter your choice? ')

    options = {'s': 'scissor', 'p': 'paper', 'r': 'rock'}
    comp = random.choice(list(options.keys()))

    print('\nYou choose %s' % options[user])
    print('Computer choose %s\n' % options[comp])

    winner = 0
    if comp == 's' and user == 'p':
        winner = 1
    elif comp == 'p' and user == 'r':
        winner = 1
    elif comp == 'r' and user == 's':
        winner = 1
    elif comp == user:
        winner = None

    if winner == 1:
        print('You lose')
    elif winner == 0:
        print('You win')
    else:
        print('Game draw')

    ans = input('\nDo you want to play again? Y/N ')
    if ans.lower() in ('y', 'yes'):
        main()


main()
