'''
Question 4
Check the validity of an IP Address
Example:
192.168.1.1 --> valid
192.168.200.199 --> valid
300.300.300.300 --> invalid
'''

import re

def checkIP(ipString):
    pattern = r'^([\d]{1,3})\.([\d]{0,3})\.([\d]{0,3})\.([\d]{0,3})$'
    ipAddress = re.findall(pattern, ipString)

    if len(ipAddress) > 0:
    	for group in ipAddress[0]:
    		num = int(group)
    		if int(group) > 255:
    			return 'invalid'
    	return 'valid'

    else:
    	return 'invalid'

def main():
    a = input('Enter a string? ')
    print(checkIP(a))


main()
