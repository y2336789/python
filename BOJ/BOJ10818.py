n = int(input())

data = list(map(int, input().split()))
min_num, max_num = data[0], data[0]

for i in range(1, len(data)):
    if min_num > data[i]:
        min_num = data[i]
    if max_num < data[i]:
        max_num = data[i]

print(min_num, max_num)