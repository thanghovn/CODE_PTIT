import math
def daoso(n):
    m=0
    while n>0:
        m = m * 10 + (n % 10)
        n//=10
    return m
t = int(input())
for _ in range(t):
    n = int(input())
    d=daoso(n)
    if math.gcd(d,n)==1:
        print('YES')
    else:
        print('NO')