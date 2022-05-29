# 계수 정렬 : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 가장 빨름
# 계수 정렬을 이용하기 위해 모든 범위를 담을 수 있는 크기의 리스트를 선언해야함

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * max(array)+1 # len(array)가 아닌 array에 있는 정수 최대값 + 1을 해줘야함

for i in range(len(array)):
    count[array[i]] = 1 

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')


