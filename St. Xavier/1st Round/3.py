'''
Question 1
Print all the fibonacci number less than 100.
For eg:- 1,1,2,3,5,8.....
'''

a = 0
b = 1
while a < 100:
    print(a)
    c = a + b
    a = b
    b = c
