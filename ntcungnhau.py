import math
n = int(input())
a = sorted(list(map(int, input().split())))
for i in range(n - 1):
    for j in range(i + 1, n):
        if math.gcd(a[j], a[i]) == 1:
            print(f"{a[i]} {a[j]}")