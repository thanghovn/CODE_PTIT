from itertools import combinations

# sàng nhỏ tới 50
def get_primes(n):
    mark = [True]*(n+1)
    mark[0]=mark[1]=False
    for i in range(2,int(n**0.5)+1):
        if mark[i]:
            for j in range(i*i,n+1,i):
                mark[j]=False
    return [i for i in range(2,n+1) if mark[i]]

def count_good(x, primes):
    if x <= 0:
        return 0

    res = x
    m = len(primes)

    for k in range(1, m+1):
        for comb in combinations(primes, k):
            prod = 1
            for v in comb:
                prod *= v
                if prod > x:
                    break
            if prod > x:
                continue

            if k & 1:
                res -= x // prod
            else:
                res += x // prod
    return res

while True:
    line = input().strip()
    if line == "-1":
        break

    L, R = map(int, line.split())
    N = int(input())

    primes = get_primes(N)

    ans = count_good(R, primes) - count_good(L-1, primes)
    print(ans)
