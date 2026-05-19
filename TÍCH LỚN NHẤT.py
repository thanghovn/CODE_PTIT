n = int(input())
a = list(map(int, input().split()))

a.sort()

res = -10**18

# 2 phần tử
res = max(res, a[-1] * a[-2])
res = max(res, a[0] * a[1])

# 3 phần tử
res = max(res, a[-1] * a[-2] * a[-3])
res = max(res, a[0] * a[1] * a[-1])

print(res)