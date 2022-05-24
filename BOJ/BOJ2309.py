data = []
s = 0
end = False
for i in range(9):
    data.append(int(input()))
    s += data[i]
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] + data[j] == s - 100:
            num1, num2 = data[i], data[j]
            data.remove(num1)
            data.remove(num2)
            end = True
            break
    if end == True: 
        break
data.sort()
for i in data:
    print(i)
    