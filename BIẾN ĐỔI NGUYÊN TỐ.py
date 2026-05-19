import math


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def distToPrime(n):
    if isprime(n): return 0
    d = 1
    while (True):
        if (n - d >= 2) and isprime(n - d): return d
        if (isprime(n + d)): return d
        d=d+1

n = int(input())
a = list(map(int , input().split()))
res=0
for s in a:
    res = max(res,distToPrime(s))
print(res)