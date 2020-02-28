'''
Question 5
Journey to the Moon
https://www.hackerrank.com/contests/aug13/challenges/journey-to-the-moon
'''

def alreadyIn(c, p):
    for i, x in enumerate(c):
        if p[0] in x or p[1] in x:
            return i, True
    return 0, False


def insertIn(c, p, i):
    if p[0] not in c[i]:
        c[i].append(p[0])

    if p[1] not in c[i]:
        c[i].append(p[1])

    return c


n, p = list(map(int, input().split()))

astro = []
for i in range(p):
    a = list(map(int, input().split()))
    astro.append(a)

countries = [] 

for pair in astro:

    index, res = alreadyIn(countries, pair)

    if res:
        countries = insertIn(countries, pair, index)
    else:
        countries.append(pair)

# print(countries)
countryNum = len(countries)

countryCount = [0 for i in range(countryNum)]

for i, l in enumerate(countries):
    countryCount[i] = len(l)
ans = 0

for i, v in enumerate(countryCount):
    ans += v * sum(countryCount[i + 1:])

print(ans)
