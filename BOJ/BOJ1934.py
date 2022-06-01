t = int(input())

def gcd(x,y):
    while y != 0:
        x, y = y, x%y
    return x

for i in range(t):
    a, b = map(int, input().split())
    print(a*b//(gcd(a,b)))