n, m = map(int, input().split()) # n : 세로,  m : 가로
d = [[0] * m for _ in range(n)] # m개의 요소가 있는 한 줄을 만든 뒤 n만큼 반복 -> n x m 생성
A, B, direction = map(int, input().split())
d[A][B] = 1 # 현재 좌표(시작 장소) 방문 체크

# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 사용자가 입력하는 n x m의 맵
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

def turn_left(direction): # 좌로 돌아 (오른쪽 : 동, 왼쪽 : 서)
    if direction == 0: direction = 3 
    else: direction -= 1 
    return direction

count = 1
turn_time = 0
while True:
    direction = turn_left(direction) # 처음에 입력받은 방향에서 왼쪽으로 돌아주기
    # print(direction)
    new_A = A + dx[direction] # 돌은 방향에 따른 새로운 좌표 계산 - 이동 시도
    new_B = B + dy[direction] # 돌은 방향에 따른 새로운 좌표 계산
    if d[new_A][new_B] == 0 and array[new_A][new_B] == 0: # 방문한 적 없는 장소 & 앞으로 나아갈 수 있는 장소 = 바다가 아닌 경우
        d[new_A][new_B] = 1 # 새로운 장소에 대해 방문 체크
        A = new_A # 새로운 장소 위치를 현재 위치로 업데이트 - 이동 실시
        B = new_B
        count += 1 
        turn_time = 0
        continue
    else : # 방문한 적이 있는 경우 or 앞으로 나아갈 수 없는 경우(바다인 경우)
        turn_time += 1
    if turn_time == 4: # 나아간 방향에서 동서남북 모두 이동할 수 없는 경우
        new_A = A - dx[direction] # 이동하기 전의 위치로 이동 시도
        new_B = B - dx[direction]
        if array[new_A][new_B] == 0 : # 이동할 수 있는 위치라면? -> 육지라면?
            A = new_A # 이동 실시
            B = new_B
        else: # 이동할 수 없는 위치라면 -> 바다라면
            break
        turn_time = 0 

print(count)
    
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1