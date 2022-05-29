n = int(input())
array = []
for i in range(n):
    a, b = input().split()
    array.append([a, int(b)])

# lambda 매개변수 : 표현식의 형태
# array 안에 있는 값을 student라함 -> ['이름', 점수(int)]
# student[0]은 '이름'을 나타내고 student[1]은 점수(int)를 나타냄
array.sort(key=lambda student : student[1])

for i in array:
    print(i[0], end = ' ')