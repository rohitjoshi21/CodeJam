'''
Question 2
Implement binary search algorithm in a given array and print the position of a target number provided from input
'''

def binarySearch(array, item):
    left = 0
    right = len(array) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = array[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


def main():
    arr = [1, 2, 4, 7, 9, 13, 15]
    target = int(input())
    index = binarySearch(arr, target)

    if index:
        print('%s is in an array of index %d' % (target, index))
    else:
        print('It is not found in array')


main()
