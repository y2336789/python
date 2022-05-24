def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return int(a * b/ gcd(a,b))

n,m = map(int, input().split())

print(gcd(n,m))
print(lcm(n,m))