def sinh(n, max_val, cur, res):
    if n == 0:
        res.append(cur[:])
        return

    for x in range(min(n, max_val), 0, -1):
        cur.append(x)
        sinh(n - x, x, cur, res)
        cur.pop()


T = int(input())

for _ in range(T):
    n = int(input())

    res = []
    sinh(n, n, [], res)

    print(len(res))

    for arr in res:
        print("(" + " ".join(map(str, arr)) + ")", end=" ")

    print()