from collections import deque

location = 0
priorities = [1,1,9,1,1,1]
alphabet = deque()
length = len(priorities)
check = dict()

for i in range(length):
    alphabet.append(chr(i+65))

find = alphabet[location]

for i in range(length):
    check[alphabet[i]] = priorities[i]
 
priorities = deque(priorities)

while True:
    isPrint = alphabet[0]
    if check[isPrint] == max(priorities):
        break
    else:
    # isPrint = priorities.popleft()
        for j in range(1, length):
            if check[alphabet[j]] > check[isPrint]:
                back = alphabet.popleft()
                alphabet.append(back)
                break

alphabet = list(alphabet)

print(alphabet)

for i in range(len(alphabet)):
    if alphabet[i] == find:
        print(i+1)
        break


# print(check)
# print(alphabet)

