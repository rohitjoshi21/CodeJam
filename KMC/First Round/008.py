'''
Question 8
Count the no of vowels from a input string
'''

def main():
	string = input('Enter your string? ')

	vowels = ['a','e','i','o','u']
	count = 0

	for c in string:
		if c.lower() in vowels:
			count += 1
			
	print(count)

#Main Execution
main()
