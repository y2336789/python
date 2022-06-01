n = int(input())
member = 0
party = 0

data = list(map(int,input().split()))
data.sort()

for i in data:
    member += 1
    if i <= member:
        party += 1
        member = 0

print(party)
