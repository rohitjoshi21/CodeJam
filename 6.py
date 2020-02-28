'''
Question 6

Go to this link for question:-
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/bricks-game-5140869d/
'''
print('Enter the elements in the array:')

array = list(map(int, input().split()))
d = int(input('Enter value of d: '))

newArray = []

N = len(array)
for i in range(N):
    index = i + d
    if index >= N:
        index = index - N
    newArray.append(array[index])

print(newArray)
