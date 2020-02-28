'''
This is a famous riddle
The snail needs to climb certain height (let say 'H')
But when it climbs some height (A)
it slips back to some height below(B)
Then we have to calculate the days or hours it will take to reach at the top or come out (let say from a well)

Eg - A snail needs to climb 30 m(H)of height in order to come out from the well.
As it climbs 2m(A) in 1 day it slips back 1m (B) below at night.
Then calculate the number of days it will take to come out.

Here,
H is 30m, A is 2m and B is 1m(from above situation)
Answer- 29 days
'''

def main():
    A, H, B = list(map(float, input().split(',')))

    day = 0
    curr = 0
    while True:
        curr += A
        day += 1
        if curr >= H:
            print(day, 'days')
            break
        curr -= B


main()
