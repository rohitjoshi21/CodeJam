'''
Question 1
Array Manipulation
Link: https://www.hackerrank.com/contests/w4/challenges/crush
'''


def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    for a, b, k in queries:
        array[a - 1] += k
        array[b] -= k

    result = acc = 0
    for x in array:
        acc += x
        result = max(result, acc)

    return result


n, m = list(map(int, input().split()))

queries = []
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)
print(result)
