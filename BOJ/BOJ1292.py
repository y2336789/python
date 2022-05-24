a,b = map(int,input().split())
data = []
result = 0 

for i in range(1, b+1):
    for j in range(i):
        data.append(i)

for i in range(a-1, b):
    result += data[i]

# arr = [0]
# for i in range(46):
#    for j in range(i):
#        arr.append(i)
# print(sum(arr[a:b+1]))

print(result)