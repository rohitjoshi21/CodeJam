'''
Question 3
2D - Array DS
https://www.hackerrank.com/contests/game-of-codes-at-snist/challenges/2d-array
'''
array = []
for i in range(6):
    line = list(map(int, input().split()))
    array.append(line)


maxSum = 0

for y in range(4):
    for x in range(4):
        a = array[y][x] + array[y][x + 1] + array[y][x + 2] + \
            array[y + 1][x + 1] + array[y + 2][x] + \
            array[y + 2][x + 1] + array[y + 2][x + 2]
        if maxSum == None or a > maxSum:
            maxSum = a


print(maxSum)
