n = int(input())
moves = list(input().split())
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
list = ['L','R','U','D']

for move in moves:
    for i in range(len(list)):
        if move == list[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny    

print(x, y)