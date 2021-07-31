def miniMaxSum(arr):
    maximum, minimum = 0, 99999999
    for i in arr:
        temp = arr.copy()
        temp.remove(i)
        curr = sum(temp)
        if curr < minimum:
            minimum = curr
        elif curr > maximum:
            maximum = curr
    print(f"{minimum} {maximum}")


def miniMaxSum(arr):
    # get a copy from the list to be able 
    # to play with
    sec = arr.copy()  # use .copy() and not = 
    arr.remove(max(arr)) # remove the maximum number 
    # this would give us tha minumum sum
    minimum = sum(arr)
    sec.remove(min(sec)) # remove the minumum number
    # this would give us the maximum sum
    maximum = sum(sec)
    print(f"{minimum} {maximum}")

def miniMaxSum(arr):
    # remove tha biggest number
    maximum_n = max(arr) 
    arr.remove(maximum_n)
    # this would give us the minimum sum
    minimum_sum = sum(arr)
    arr.append(maximum_n)  # don't forget to turn it back
    # remove the minumum number
    minimum_n = min(arr)
    arr.remove(minimum_n)
    # this would give us the maximum sum
    maximum_sum = sum(arr)
    print(f"{minimum_sum} {maximum_sum}")
