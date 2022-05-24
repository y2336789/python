people = 0
now = 0
max_people = 0

for i in range(10):
    a, b = map(int, input().split())
    people -=a
    people += b
    now = people
    if people > max_people:
        max_people = now

print(max_people)