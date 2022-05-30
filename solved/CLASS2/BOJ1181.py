n = int(input())
data = []

for _ in range(n):
    data.append(input())

data = list(set(data))

data.sort(key = lambda x : len(x))

print(data)