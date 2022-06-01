s = input()
part_zero = 0
part_one = 0

if s[0] == '0':
    part_zero += 1
else:
    part_one += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            part_zero += 1
        else:
            part_one += 1

print(min(part_one, part_zero))