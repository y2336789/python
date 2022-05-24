from collections import deque
import sys
n = int(sys.stdin.readline())
data = deque()

for i in range(n):
    command= sys.stdin.readline().split()
    if 'push' in command:
        data.append(command[1])
    elif 'pop' in command:
        if len(data) == 0:
            print(-1)
        else: print(data.popleft())  
    elif 'front' in command:
        if len(data) == 0: print(-1)
        else: print(data[0])
    elif 'back' in command:
        if len(data) == 0: print(-1)
        else: print(data[len(data)-1])
    elif 'size' in command:
        print(len(data))
    elif 'empty' in command:
        if len(data) == 0:
            print(1)
        else: print(0)
