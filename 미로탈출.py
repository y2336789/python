from collections import deque

n,m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

move = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y): # bfs 이용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 무한 반복
    while queue: 
        x, y = queue.popleft() # FIFO
        # 상 하 좌 우 순서대로 계산
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            # 다음에 움직일 좌표에 대해 검사
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue # for문으로 다시 돌아가서 다른 방향
            # 0인 칸은 갈 수 없음
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                # 시작 지점 값 1부터 이동 가능한 다음 칸으로 이동하면서 값을 더해줌
                graph[nx][ny] += graph[x][y] 
                queue.append((nx,ny)) # 이동을 마친 새로 도착한 칸에 대해서 queue에 삽입
    return graph[n-1][m-1]

print(bfs(0,0))




