n, m = map(int, input().split())
for i in range(n//2):
    string = ((i * 2 ) + 1 ) * ".|."
    print(string.center(m, "-"))
print("WELCOME".center(m,"-"))
for j in range(n//2):
    string = (n-(2*(j+1))) * ".|."
    print(string.center(m,"-"))
