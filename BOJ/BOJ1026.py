# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# data = dict()
# sum = 0

# for i in range(n):
#     max_b = max(b)
#     min_a = min(a)
#     data[max_b] = min_a
#     b.remove(max_b)
#     a.remove(min_a)

# for i in data:
#     sum += i * data[i]

# print(sum)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
sum = 0
for i in range(n):
    sum += a[i] * max(b)
    b.pop(b.index(max(b)))

print(sum)