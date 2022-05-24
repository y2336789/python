from collections import Counter
from itertools import count

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 변환