from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data) # deque([]) 형태로 출력됨
print(list(data))