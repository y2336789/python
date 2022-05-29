from collections import deque
n, m, v = map(int, input().split())

data = [[] for x in range(n+1)]
# DFS 전용 체크 visited
visited = [False] * (n+1)
# BFS 전용 체크 visited1
visited2 = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

for i in range(len(data)):
    data[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(data, v, visited)
print()
bfs(data, v, visited2)