input_data = input()

row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1 # 문자열의 첫번재 알파벳 - ord('a) + 1 -> 첫 번째 칸이 1부터 시작하기 때문
# ord('a') = 97 ord('A') = 65
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

count = 0
for step in steps:
    new_row = row + step[0]
    new_column = column + step[1]
    if new_row >= 1 and new_row <= 8 and new_column >=1 and new_column <= 8 :
        count += 1

print(count)