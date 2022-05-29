array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start <= end:
        return
    pivot = array[start]
    left = start + 1
    right = end
    while left <= right:
        # array[left] 값이 array[pivot]값보다 커지는 index를 찾는 코드
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # array[right] 값이 array[pivot]값보다 작아지는 index를 찾는 코드
        while start < right and array[right] >= array[pivot]:
            right -= 1
        # left index와 right index가 교차 역전했을 경우
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 엇갈리지 않고 pivot 위치의 값보다 큰 데이터와 작은 데이터를 찾은 경우
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)