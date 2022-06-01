n = int(input())
result = 0

data = list(map(int, input().split()))
data.sort()
min_time = []

for i in data:
    result += i
    min_time.append(result)

print(sum(min_time))
