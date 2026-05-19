MAXN = 10**6 + 10

prime = [True] * MAXN
prime[0] = prime[1] = False

for i in range(2, int(MAXN**0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAXN, i):
            prime[j] = False


def count_triplet(N):
    cnt = 0
    for p in range(2, N - 5):
        if prime[p]:
            # dạng (p, p+2, p+6)
            if prime[p+2] and prime[p+6]:
                cnt += 1
            # dạng (p, p+4, p+6)
            elif prime[p+4] and prime[p+6]:
                cnt += 1
    return cnt


# ===== MAIN =====
t = int(input())
for _ in range(t):
    n = int(input())
    print(count_triplet(n))