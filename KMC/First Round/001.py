'''
Question 1
Print the following pattern:
   / \
  /   \
 /     \
 -------
'''


def main():
    initialSpace = 3
    midSpace = 1

    string = '{0}/{1}\\'

    for i in range(3):
        print(string.format(initialSpace * ' ', midSpace * ' '))
        midSpace += 2
        initialSpace -= 1

    print(' -------')


main()
