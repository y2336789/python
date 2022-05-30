n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

# 피보나치와 동일하게 첫 번째 원소와 두번째 원소에 대해서는 바로 DP 테이블에 값을 넣어줌
d[0] = array[0]
d[1] = max(array[0], array[1])

# 세번째 원소(2번 index)부터는 해당 점화식에 의해 값이 진행
for i in range(2, n):
    # 만약 i-1번째 방 + i-3 + i-5 + ... 의 방을 쭉 털어오는 게 이득인 경우 vs 현재 방도 털고 그 이전의 방부터 index로는 i-2칸 방 부터 2칸 떨어진 모든 방을 터는 경우
    d[i] = max(d[i-1], d[i-2] + array[i])
    
# 리스트 길이 고려해서 n-1을 넣어줌
print(d[n-1])