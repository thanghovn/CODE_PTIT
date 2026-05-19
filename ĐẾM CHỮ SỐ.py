def solve(n):
    cnt = [0] * 10

    if n <= 0:
        return cnt

    factor = 1

    while factor <= n:
        lower = n % factor
        cur = (n // factor) % 10
        higher = n // (factor * 10)

        for d in range(10):
            cnt[d] += higher * factor

        for d in range(cur):
            cnt[d] += factor

        cnt[cur] += lower + 1

        cnt[0] -= factor

        factor *= 10

    return cnt


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    left = solve(A - 1)
    right = solve(B)

    ans = [right[i] - left[i] for i in range(10)]

    print(*ans)