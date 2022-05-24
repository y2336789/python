from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]: # ex) graph[1][1] : 1번 노드에 연결된 2번 노드 검사
            if not visited[i]: # 방문하지 않았다면
                queue.append(i) # insert 실행
                visited[i] = True  # insert 후 방문 처리

graph = [
    [], 
    [2,3,8], # 1번 노드와 연결된 노드
    [1,7], # 2번 노드와 연결된 노드
    [1,4,5], # 3번 노드와 연결된 노드
    [3,5], # 4번 노드와 연결된 노드
    [3,4], # 5번 노드와 연결된 노드
    [7], # 6번 노드와 연결된 노드
    [2,6,8], # 7번 노드와 연결된 노드
    [1,7] # 8번 노드와 연결된 노드
]

visited = [False] * 9

bfs(graph, 1, visited)