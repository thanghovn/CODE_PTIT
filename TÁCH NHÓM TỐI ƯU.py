n, k = map(int, input().split())
A = list(map(int, input().split()))

if n == 0:
    print(0)
    exit()

A.sort()

groups = 1  # ít nhất 1 nhóm
count = 1   # số phần tử trong block hiện tại

for i in range(1, n):
    if A[i] - A[i-1] <= k:
        count += 1
    else:
        # kết thúc 1 block → tạo nhóm mới
        groups += 1
        count = 1

print(groups)