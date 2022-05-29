m = int(input())
n = int(input())
data = []

for i in range(m, n+1):
    count = 0
    if i != 1:
        for j in range(1, i+1):
            if i % j == 0:
                count +=1
    if count == 2:
        data.append(i)

if len(data) != 0:
    print(sum(data))
    print(data[0])
else:
    print(-1)