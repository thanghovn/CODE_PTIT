import math
def songto(n):
    if (n < 2):
        return False
    i = 2
    while i * i <= n:
        if (n%i==0):
            return False
        i+=1
    return True

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = int(math.gcd(a, b))
    sum = 0
    while (c > 0):
        sum +=c%10
        c//=10
    if (songto(sum)) :
        print('YES')
    else :
        print('NO')