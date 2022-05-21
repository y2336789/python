from collections import defaultdict

n = int(input())
sangguen = defaultdict()

data = list(map(int, input().split()))
for i in range(n):
    sangguen[data[i]] = 1

m = int(input())
data2 = list(map(int, input().split()))

for i in range(m):
    if data2[i] in sangguen.keys():
        print(1, end=' ')
    else:
        print(0, end=' ')