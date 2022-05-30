# n = int(input())
# n_array = list(map(int, input().split()))
# m = int(input())
# m_array = list(map(int, input().split()))

# data = [0] * (max(n_array) + 1)

# for i in n_array:
#     data[i] = 1

# for i in m_array:
#     if data[i] != 1:
#         print('no', end=' ')
#     else:
#         print('yes', end=' ')    

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            end = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

