from sklearn.preprocessing import binarize


t = int(input())

for _ in range(t):
    n = int(input())
    data = str(bin(n))[2:]
    for i in range(len(data)):
        if data[-i-1] == '1':
            print(i, end=' ')
         