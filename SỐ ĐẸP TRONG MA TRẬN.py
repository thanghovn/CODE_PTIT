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

# tính số may mắn
lucky = max_val - min_val

found = False

# tìm và in vị trí
for i in range(n):
    for j in range(m):
        if A[i][j] == lucky:
            if not found:
                print(lucky)
                found = True
            print(f"Vi tri [{i}][{j}]")

if not found:
    print("NOT FOUND")