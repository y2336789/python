n = int(input())
data = list(map(int, input().split()))

m = int(input())
data2 = list(map(int, input().split()))

data.sort()

def function(data, num, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if num == data[mid]:
        return True
    elif num < data[mid]:
        return function(data, num, start, mid-1)
    else :
        return function(data, num, mid+1, end)


for i in data2:
    if function(data, i, 0, n-1) == True:
        print(1)
    else : print(0)

    




