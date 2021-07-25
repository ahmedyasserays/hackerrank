n = int(input())
for i in range(n):
    print(i+1, end="")

# another solution
ans =''
for i in range(n):
    ans += str(i+1)
print(ans)