n = int(input())
m = int(input())

count = 0

graph = [[] for n in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, visited, start):
    global count
    visited[start] = True
    for node_num in graph[start]:
        if visited[node_num] == False:
            visited[node_num] = True
            dfs(graph, visited, node_num)
            count +=1
    return count

print(dfs(graph, visited, 1))
    
