from bisect import bisect_left, bisect_right
from operator import le
# 정렬된 리스트에서 사용해야함 -> 이진 탐색에 매우 효율적임

# a = [1,2,4,4,8]
# x = 4

# print(bisect_left(a,x)) # 정렬된 a 리스트에서 x를 집어넣을 가장 왼쪽 인덱스를 찾기
# print(bisect_right(a,x)) # 정렬된 a 리스트에서 x를 집어넣을 가장 오쪽 인덱스를 찾기1

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print(right_index, left_index)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 9)) # 값이 4인 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 값이 -1 ~ 3인 데이터 개수 출력
