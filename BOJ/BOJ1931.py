n = int(input())
data = []

for i in range(n):
    a, b = map(int, input().split())
    data.append((a,b))

data.sort(key = lambda x : x[0])
data.sort(key= lambda x : x[1])

# print(data)

count = 1
end = data[0][1]

for i in range(1, n):
    if data[i][0] >= end :
        count +=1
        end = data[i][1]

print(count)