n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() 

firstMax = max(data)
secondMax = data[len(data)-2]
result = 0

firstCount = (m // (k+1)) * k
firstCount += (m % (k+1))
secondCount = 8 - firstCount

result += firstMax * firstCount
result += secondCount * secondMax

print(result)


