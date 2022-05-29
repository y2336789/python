import heapq # 파이썬에선 힙에 원소를 넣었다가 빼는 것 만으로도 O(NlogN)에 오름차순 정렬이 완료됨

def heapsort(iterable): # 최소 힙
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value) # value 값을 h에 삽입
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

def max_heapsort(iterable): # 최대 힙 : 순서 역순
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value) # 임시로 원소의 부호를 변경
    for _ in range(len(h)) : # 힙에서 원소를 꺼낸 뒤에 원소의 부호 바꾸기
        result.append(-heapq.heappop(h)) # 꺼낼 때는 최소 힙 - 즉 낮은 원소부터 꺼내기 때문
    return result

result = max_heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
