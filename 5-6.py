INF = 999999999 # 무한의 비용

# 2차원 리스트를 통해 인접 행렬 표현(그래프)
graph = [
    [0,7,5],
    [7,0,INF], # 간선으로 연결되지 않은 노드끼리는 무한의 비용, 자기 자신은 0으로
    [5,INF,0]
]

print(graph)