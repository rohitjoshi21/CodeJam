'''
Question 5
Read a file with given input name and print its 3rd line
'''


def main():
    filename = input()

    file = open(filename, 'r')
    data = file.readlines()
    file.close()

    # Printing 3rd Line
    print(data[2])


main()
