# graph : 노드 연결 정보를 담고 있는 2차원 리스트, v : 방문하고자 하는 노드, visited : 방문 처리를 나타내는 1차원 리스트
def DFS(graph, v, visited):

    visited[v] = True
    print(v, end='')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, v, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트), 거리 정보는 없음
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

visited =[False] * len(graph)

DFS(graph, 1, visited)