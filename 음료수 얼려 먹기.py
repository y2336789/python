n, m = map(int, input().split())
result = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    # 인덱스의 범위가 0 ~ n-1 / 0 ~ m-1 이니까 -1과 n과 m으로 구분
    if x <= -1 or x >= n or y <= -1 or y >= m: 
        return False
    if graph[x][y] == 0: # 현 위치에 대해 1과 0 판정
        graph[x][y] = 1
        # 상 하 좌 우에 대해서 dfs 재귀 실행
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        # 특정 위치에서 0-0-0 뭉치를 다 탐색했을 경우 True 반환 및 카운트
        if dfs(i,j) == True:
            result +=1
print(result)