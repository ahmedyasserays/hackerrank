def maxSubarrayValue(arr):
    # Write your code here
    maximum = -999999
    start = pointer = 0
    curr = 0
    while start < len(arr):
        if pointer % 2 == 0:
            curr += arr[start + pointer]
        else:
            curr -= arr[start + pointer]
            
        if curr > maximum:
            maximum = curr
        pointer += 1
        
        if curr < 1 or pointer + start == len(arr):
            start += 1
            pointer = 0
            curr = 0
        
    
    minimum = 999999
    start = pointer = 0


    curr = 0
    while start < len(arr):
        if pointer  % 2 == 0:
            curr += arr[start + pointer]
        else:
            curr -= arr[start + pointer]
            
        if curr <minimum:
            minimum = curr
        pointer += 1
        
        if curr < 1 or pointer + start == len(arr):
            curr = 0
            start += 1
            pointer = 0
    return max(maximum**2, minimum**2)

arr = [-1,
2,
3,
4,
-5]

# print(maxSubarrayValue(arr))

def maxSubarrayValue(arr):    
    pointer = 0
    score = 0
    i = 0
    checkpoint = 0
    maximum = -9999999
    while i < len(arr):
        element = arr[i]
        if pointer % 2 == 0:
            score += element
        else:
            score -= element
        pointer += 1
        i += 1
        if score > maximum:
            maximum = score
        if score < 1:
            pointer = 0
            score = 0
            i = checkpoint +1
            checkpoint = i
    maximum = maximum**2
    
    pointer = 0
    score = 0
    i = 0
    checkpoint = 0
    mimimum = 999999
    while i < len(arr):
        element = arr[i]
        if pointer % 2 == 0:
            score += element
        else:
            score -= element
        pointer += 1
        i += 1
        if score < mimimum:
            mimimum = score
        if score > -1:
            pointer = 0
            score = 0
            i = checkpoint +1
            checkpoint = i
    mimimum = mimimum**2
    return max(maximum, mimimum)

arr = [6,
3,
-1,
-1,
-1,
5,
1,
]
print(maxSubarrayValue(arr))
