n = int(input())

graph = []
home_count = []
home = 0

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global home
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        home += 1
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False # 현재 찾는 위치의 값이 0인 경우

count = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            count += 1
            home_count.append(home)
            home = 0

print(count)
home_count.sort()
for i in home_count:
    print(i)