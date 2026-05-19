n = int(input())
a = list(map(int, input().split()))

mx = max(a)

ans = 0
cnt = 0

for x in a:
    if x == mx:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)