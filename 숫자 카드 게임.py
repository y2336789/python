n, m = map(int, input().split())
minlist = list()

# maxValue = 0
for _ in range(n):
    cardlist = map(int, input().split())
    minValue = min(cardlist)
    minlist.append(minValue)
    # maxValue = max(minValue, maxValue)

print(max(minlist))
#print(maxValue)