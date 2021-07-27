def diagonalDifference(arr):
    length = len(arr) # finding the length of the list
    first = 0           # note that the 2 dimensions are equal
    second = 0    # initial start with zero for both diagonals
    for i in range(length):
        first += arr[i][i]   
        second += arr[i][length - i - 1]
    return abs(first- second)  # returns the absolute value