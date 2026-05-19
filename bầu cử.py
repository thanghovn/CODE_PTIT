N, M = map(int, input().split())

# Đếm phiếu
L = [0] * (M + 1)
for vote in map(int, input().split()):
    L[vote] += 1
# Tìm số phiếu cao nhất
max1 = max(L)

for i in range(1, M + 1):
    if L[i] == max1:
        L[i] = 0

# Tìm số phiếu cao thứ hai
max2 = max(L)

if max2 != 0:
    print(L.index(max2))
else:
    print("NONE")