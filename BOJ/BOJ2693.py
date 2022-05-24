t = int(input())

for i in range(t):
    count = 0
    data = list(map(int, input().split()))
    data.sort()
    result = data[0]
    for j in range(1, len(data)):
        if count == 7:
            break
        else:
            if result < data[j]:
                result = data[j]
                count += 1
    print(data[count])
        
        