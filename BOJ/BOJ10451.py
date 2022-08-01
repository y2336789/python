T = int(input())

def dfs(x):
    visited[x] = True
    next = answer[x]
    if not visited[next]:
        dfs(next)

for i in range(T):
    result = 0
    N = int(input())
    answer = [0] + list(map(int, input().split()))
    visited =  [False] * (N+1)


    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            result +=1
    print(result)

    
