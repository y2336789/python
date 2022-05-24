n = int(input())
data = list(map(int, input().split()))
result = []

for i in data:
    count = 0
    if i != 1:
        for j in range(1, i+1):
            if i % j == 0:
                count +=1 
        
    if count == 2:
        result.append(i)
        
# print(result)
print(len(result))