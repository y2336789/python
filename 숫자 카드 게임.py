n, m = map(int, input().split())
minlist = list()

for _ in range(n):
    cardlist = map(int, input().split())
    minValue = min(cardlist)
    minlist.append(minValue)

print(max(minlist))