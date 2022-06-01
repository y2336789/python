# s = list(map(int, input()))
# s.sort()
# count = 0

# while 0 in s:
#     s.remove(0)

# count += s[0]
# for i in range(1, len(s)):
#     count *= s[i]

# print(count)

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num
    
print(result)