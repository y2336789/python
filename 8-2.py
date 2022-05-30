# 한 번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 만약에 이미 계산한 적이 있는 fibo라면
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# d = [0] * 100

# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3, n+1):
#     d[i] = d[i-1] + d[i-2]

# print(d[n])