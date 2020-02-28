'''
Question 4
Check if the number is valid or not with following criteria:
  ** The first digit should contain number between 7 to 9.
  ** The rest 9 digit can contain any number between 0 to 9.
  ** The mobile number can be of 11 digits also by including 0 at the starting.
  ** The mobile number can be of 12 digits also by including 91 at the starting.

The number which satisfies the above criteria is a valid mobile number.
'''
import re

num = input('Enter Mobile Number:\n')

patt1 = '^[789][0-9]{9}$'
patt2 = '^0[789][0-9]{9}$'
patt3 = '^91[789][0-9]{9}$'

if re.match(patt1, num) or re.match(patt2, num) or re.match(patt3, num):
    print('Valid Mobile Number')
else:
    print('Invalid Mobile Number')
