t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = 0
    for x in a:
        res ^= x

    print(res)