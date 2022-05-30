# 간단한 다익스트라 알고리즘 소스코드
from math import dist
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)] # 입력한 n까지 연결 리스트를 만들기 위해 n+1까지 선언 , 0은 안씀 
visited = [False] * (n+1) # 방문 한것을 체크하는 visited도 0은 안씀
distance = [INF] * (n+1) # graph와 visited 외에도 distance를 사용한다

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # a번 노드와 b번 노드가 연결되었는데 간선 거리는 c를 의미함

# 방문하지 않은 전체 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환한다.
def get_smallest_node():
    min_value = INF
    index = 0 
    for i in range(1, n+1): # 0번 노드는 존재하지 않으니 1번 노드부터 n까지 반복
        # 아직 방문하지 않은 노드이고 기존의 최단 거리보다 거리가 짧은 경우를 찾음, min_value가 가장 작은 노드의 index를 반환해줌
        if distance[i] < min_value and not visited[i]: 
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작점에 대한 distance는 0
    visited[start] = True
    for j in graph[start]: # j : (b,c)로 이루어져 있음, start에 연결된 (b,c)와 같은 정보들을 j로 불러옴
        distance[j[0]] = j[1] # j[0] : 연결된 노드, j[1] : 연결된 노드까지의 간선 거리, start에 연결된 점들에 대해 거리 설정
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복  
    for i in range(n-1): 
        now = get_smallest_node()
        visited[now] = True
        # 현재 가장 짧은 거리로 인해 선택된 노드와 연결된 다른 노드를 확인한다.
        for j in graph[now]: # 선택된 노드에서 (b,c)를 불러옴, 해당 노드를 거쳐서 갈 수 있는 노드들을 탐색
            cost = distance[now] + j[1] # 자신이 선택되었을때 최단 거리 + 자신으로부터 목적지까지의 노드 거리
            if cost < distance[[j[0]]]: # 자신으로부터 목적지까지의 거리 값 비교를 통해 값이 작을 시 짧은 거리로 update
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한을 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])