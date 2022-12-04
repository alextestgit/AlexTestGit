# How do you find the missing number in a given integer array of 1 to 100
test = {1: [[0, 1, 2, 3, 5, 6, 8, 10], [4, 7]]}


def missing_number(arr):
    print([a for a in range(arr[0],arr[-1]+1) if a not in arr])


missing_number([2, 1, 0, 3, 5, 6, 8, 10])
