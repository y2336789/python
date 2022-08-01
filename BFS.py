# 가까운 노드부터 탐색
# 선입선출 방식인 Queue 자료구조를 이용하는1

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 괄호 안의 [start]의 의미 : 첫 시작 노드를 큐에 넣는 의미
    visited[start] = True # 방문 처리
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [], # 0번 노드부터 시작
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)