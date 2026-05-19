n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]

# tính A[0]
a0 = (B[0][1] + B[0][2] - B[1][2]) // 2

A = [0] * n
A[0] = a0

# tính các phần tử còn lại
for i in range(1, n):
    A[i] = B[0][i] - a0

print(*A)