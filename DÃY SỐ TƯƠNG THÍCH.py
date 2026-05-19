n = int(input())
a = list(map(int, input().split()))

INF = 10**18
ans = INF

mx = max(a)

for k in range(mx + 1):
    s = 0
    ok = True

    for x in a:
        b = x // (k + 1) + 1

        if x // b != k:
            ok = False
            break

        s += b

    if ok:
        ans = min(ans, s)

print(ans)