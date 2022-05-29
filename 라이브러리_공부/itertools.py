from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(permutations(data, 3)) # 순열
print(result)
result = list(combinations(data, 2)) # 조합(컴비네이션)
print(result)
result = list(product(data, repeat=2)) # 중복있는 순열
print(result)
result = list(combinations_with_replacement(data, 2)) # 중복있는 조합
print(result)
