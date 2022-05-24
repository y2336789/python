n = int(input())
moves = list(input().split())
x, y = 1, 1 

# 각각 L, R, U, D 순서에 맞게 증감을 나타냄
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
list = ['L','R','U','D']

for move in moves:
    for i in range(len(list)):
        if move == list[i]:
            nx = x + dx[i] # ex) R로 움직이면 x는 변함 없음
            ny = y + dy[i] # ex) R로 움직이면 y는 +1 : (1,1)에서 (1,2)로
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue # 이 밑의 코드들은 무시 후 다시 맨 처음 for문으로 돌아감
    x, y = nx, ny 

print(x, y)