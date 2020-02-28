'''
Question 2
Perform 2x2 matrix multiplication and print the result.
'''

a, b, c, d = map(int, input().split())
p, q, r, s = map(int, input().split())


answer = [[a * p + b * r, a * q + b * s],

          [c * p + d * r, c * q + d * s]]

print('\nThe product is: ')
print(answer[0])
print(answer[1])
