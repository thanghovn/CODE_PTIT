n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

sum_upper = 0
sum_lower = 0

for i in range(n):
    for j in range(n):
        if i < j:
            sum_upper += a[i][j]
        elif i > j:
            sum_lower += a[i][j]

diff = abs(sum_upper - sum_lower)

# in kết quả
if diff <= k:
    print("YES")
else:
    print("NO")

print(diff)