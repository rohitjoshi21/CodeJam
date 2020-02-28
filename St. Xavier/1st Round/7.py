'''
Question 7
Print the pattern:
1
22
333
4444
55555
'''
a = 1
for i in range(1, 6):
    print(a * i)
    a = a * 10 + 1
