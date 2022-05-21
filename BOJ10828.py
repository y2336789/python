import sys
n = int(sys.stdin.readline())
data = []

for i in range(n):
    command= sys.stdin.readline().split()
    if 'push' in command:
        data.append(command[1])
    elif 'pop' in command:
        if len(data) == 0:
            print(-1)
        else : print(data.pop())  
    elif 'top' in command:
        if len(data) == 0:
            print(-1)
        else:
            print(data[len(data)-1])
    elif 'size' in command:
        print(len(data))
    elif 'empty' in command:
        if len(data) == 0:
            print(1)
        else: print(0)