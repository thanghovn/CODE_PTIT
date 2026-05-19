t = int(input())

for _ in range(t):
    n, p = map(int, input().split())

    ans = 0
    while n:
        n //= p
        ans += n

    print(ans)