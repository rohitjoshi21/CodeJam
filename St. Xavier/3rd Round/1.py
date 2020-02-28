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
