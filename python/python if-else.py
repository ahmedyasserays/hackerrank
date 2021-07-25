n = int(input().strip())
if n %2 != 0 or (n >= 6 and n < 21) :
    print('Weird')
else:
    print('Not Weird')