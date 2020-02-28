'''
Question 1
How do you find the largest and smallest number in a unsorted integer array?
'''

print('Enter the elements in the array:')

array = list(map(int, input().split()))

maxM = None
minM = None
for i in array:

    if maxM == None:
        maxM = i
        minM = i

    if i > maxM:
        maxM = i
    elif i < minM:
        minM = i

print('Maximum no is', maxM)
print('Minimum no is', minM)
