'''
Question 8

Go to this link for question:-
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/
'''


def getSteps(a, b):
    a = list(a)
    b = list(b)

    for i in a[:]:
        if i in b:
            a.remove(i)
            b.remove(i)

    return len(a) + len(b)


t = int(input())
for _ in range(t):
    a = input()
    b = input()

    print(getSteps(a, b))
