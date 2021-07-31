N = int(input())
myList = []
for i in range(N):
    commands = input().split(' ')
    if commands[0] == 'append':
        myList.append(int(commands[1]))
    elif commands[0] == 'print':
        print(myList)
    elif commands[0] == 'insert':
        myList.insert(int(commands[1]), int(commands[2]))
    elif commands[0] == 'remove':
        myList.remove(int(commands[1]))
    elif commands[0] == 'sort':
        myList.sort()
    elif commands[0] == 'reverse':
        myList.reverse()
    elif commands[0] == 'pop':
        myList.pop()