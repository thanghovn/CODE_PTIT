def giao(a, b, n, m):
    i = j = 0
    res = []

    while i < n and j < m:
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(*res)


def atrub(a, b, n, m):
    i = j = 0
    res = []

    while i < n and j < m:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
            j += 1

    while i < n:
        res.append(a[i])
        i += 1

    print(*res)


# INPUT
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 🔥 QUAN TRỌNG
a = sorted(set(a))
b = sorted(set(b))

n = len(a)
m = len(b)

# OUTPUT
giao(a, b, n, m)
atrub(a, b, n, m)
atrub(b, a, m, n)