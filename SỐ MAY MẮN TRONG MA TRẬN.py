n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# tìm min và max
min_val = float('inf')
max_val = float('-inf')

for i in range(n):
    for j in range(m):
        if A[i][j] < min_val:
            min_val = A[i][j]
        if A[i][j] > max_val:
            max_val = A[i][j]

# số may mắn
lucky = max_val - min_val

# tìm vị trí
positions = []

for i in range(n):
    for j in range(m):
        if A[i][j] == lucky:
            positions.append((i, j))

# output
if not positions:
    print("NOT FOUND")
else:
    print(lucky)
    for i, j in positions:
        print(f"Vi tri [{i}][{j}]")