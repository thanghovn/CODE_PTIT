n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# Trường hợp 1: xóa hàng
if n > m:
    remove = n - m
    newA = []

    for i in range(n):
        # i % 2 == 0 <=> hàng lẻ (1-based)
        if i % 2 == 0 and remove > 0:
            remove -= 1
            continue
        newA.append(A[i])

    A = newA

# Trường hợp 2: xóa cột
elif m > n:
    remove = m - n
    keep_cols = []

    for j in range(m):
        # j % 2 == 1 <=> cột chẵn (1-based)
        if j % 2 == 1 and remove > 0:
            remove -= 1
            continue
        keep_cols.append(j)

    newA = []
    for row in A:
        new_row = [row[j] for j in keep_cols]
        newA.append(new_row)

    A = newA

# In kết quả
for row in A:
    print(*row)