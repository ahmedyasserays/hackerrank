x, y, z= 3, 5, 7  # for example
n = 9  # on hacker rank just input these numbers

# using the list comprehensions 
result = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)] 
print(result)

# this gives the same result using for loops
result = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                result.append([i, j, k])

print(result)
