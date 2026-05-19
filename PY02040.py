n = int(input())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
k = int(input())
sum_tren = 0
sum_duoi = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            sum_tren += matrix[i][j]
        elif i + j >= n:
            sum_duoi += matrix[i][j]
diff = abs(sum_tren - sum_duoi)
if diff <= k :
    print('YES')
else:
    print('NO')
print (diff)