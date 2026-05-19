import math
from math import gcd

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def prime_min(n):
    cnt =0
    for i in range (1,n + 1):
        if math.gcd(n,i)==1:
            cnt += 1
    return cnt

s = int(input())
for i in range(s) :
    val = int(input())
    k = prime_min(val)
    if is_prime(k) :
        print('YES')
    else :
        print('NO')
