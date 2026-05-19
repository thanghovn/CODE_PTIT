MAXN = 10**6 + 10


prime = [True] * MAXN
prime[0] = prime[1] = False

for i in range(2, int(MAXN**0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAXN, i):
            prime[j] = False


def solve(n):
    res = []
    for i in range(2, n):
        if prime[i]:
            rev = int(str(i)[::-1])
            if rev != i and rev < n and prime[rev] and i < rev:
                res.append(f"{i} {rev}")
    print(" ".join(res))



t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)