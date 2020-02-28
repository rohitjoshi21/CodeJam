'''
Question 1
Get the enter and exit time of an employeer of 6 days. Get the per hour salary. 
Calculate total wage of the employee if 50% extra salary is provided for overtime
hours. If 40 hours is the normal working hours, print the total wage.
Eg:
Enter the entering and exiting time of 6 days:- 
10:00am 04:00pm
09:30am 03:30pm
10:00am 05:00pm
08:10am 07:00pm
04:00am 10:00am
10:00am 04:00pm

Enter Salary per hour:-  11000

The total wage is 470250.00 
'''

def getTime(raw):
    hour = raw[:2]
    mins = raw[3:5]
    mode = raw[5:]

    return int(hour), int(mins), mode


def getTimes():
    times = []

    print('\nEnter the entering and exiting time of 6 days:- ')
    for i in range(6):
        start, end = input().split()
        times.append([start, end])

    return times


times = getTimes()
salary = int(input('\nEnter Salary per hour:-  '))

totalHr = 0
for day in times:

    h1, m1, p1 = getTime(day[0])
    h2, m2, p2 = getTime(day[1])

    if 'pm' in p1.lower():
        h1 += 12
    if 'pm' in p2.lower():
        h2 += 12

    diffHr = ((h2 * 60 + m2) - (h1 * 60 + m1)) / 60
    totalHr += diffHr

if totalHr <= 40:
    totalSal = totalHr * salary
else:
    totalSal = 40 * salary + (totalHr - 40) * salary * 1.5

print('\nThe total wage is %.2f ' % totalSal)
