from collections import deque

n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

moves = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(len(moves)):
            nx = x + moves[i][0]
            ny = y + moves[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))



