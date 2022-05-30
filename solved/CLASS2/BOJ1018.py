n, m = map(int, input().split())

data = []
result = []

for i in range(n):
    data.append(input())

# 4가지 케이스 1) 8x8일 경우 2) 가로만 8 초과 3) 세로만 8 초과 4) 전부 8 초과
# 4) n과 m이 8 x 8 이상일 때 나올 수 있는 8x8 체스판의 개수는 n - 7 * n - 7 개
# 8x8 이상의 체스판이 선언될 수 있기에 이에 대해 8x8 체스판을 체크할 위치를 정하는 이중 for문
for x in range(n-7): 
    for y in range(m-7): 
        miss1 = 0 # (x,y)를 시작으로 8x8 체스판을 설정했다면 miss1과 miss2 초기화
        miss2 = 0
        for a in range(x, x+8): # 정한 위치를 토대로 0 ~ 8 까지 세로
            for b in range(y, y+8): # 0 ~ 8 까지 체스판 한칸 씩 체크
                if (b+a) % 2 == 0: # 짝수 칸일 경우
                    if data[a][b] != 'W': miss1 += 1 # 첫 시작 칸이 'B'일 경우의 새로 칠해야할 횟수
                    if data[a][b] != 'B': miss2 += 1 # 첫 시작 칸이 'W'일 경우 새로 칠해야할 횟수
                else:
                    if data[a][b] != 'B': miss1 += 1
                    if data[a][b] != 'W': miss2 += 1
        result.append(miss1)
        result.append(miss2)

print(min(result))

