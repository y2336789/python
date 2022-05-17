n, m = map(int, input().split()) # n : 세로,  m : 가로
d = [[0] * m for _ in range(n)]
A, B, direction = map(int, input().split())
d[A][B] = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

def turn_left(direction):
    if direction == 0: direction = 3
    else: direction -= 1
    return direction

count = 1
turn_time = 0
while True:
    direction = turn_left(direction)
    # print(direction)
    new_A = A + dx[direction]
    new_B = B + dy[direction]
    if d[new_A][new_B] == 0 and array[new_A][new_B] == 0:
        d[new_A][new_B] = 1
        A = new_A
        B = new_B
        count += 1
        turn_time = 0
        continue
    else :
        turn_time += 1
    if turn_time == 4:
        new_A = A - dx[direction]
        new_B = B - dx[direction]
        if array[new_A][new_B] == 0 :
            A = new_A
            B = new_B
        else:
            break 
        turn_time = 0

print(count)
    
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1