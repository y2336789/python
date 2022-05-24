def dfs(graph, v, visited): # graph: 그래프, v : 방문한 노드 번호, visited : 방문 여부 저장
    # 현재 노드에 대한 방문을 처리
    visited[v] = True
    print(v,'번 노드 방문')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [], # graph[0]
    [2,3,8], # graph[1], 1번 노드와 연결된 노드
    [1,7], # 2번 노드와 연결된 노드
    [1,4,5], # 3번 노드와 연결된 노드
    [3,5], # 4번 노드와 연결된 노드
    [3,4], # 5번 노드와 연결된 노드
    [7], # 6번 노드와 연결된 노드
    [2,6,8], # 7번 노드와 연결된 노드
    [1,7] # 8번 노드와 연결된 노드
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

dfs(graph, 1, visited)
