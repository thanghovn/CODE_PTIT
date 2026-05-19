def to_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    res = []

    for j in range(10, n):
        r = int(str(j)[::-1])
        if r > n:
            break
        if j != r and j < r:
            if to_prime(j) and to_prime(r):
                res.append(j)
                res.append(r)

    print(*res)
