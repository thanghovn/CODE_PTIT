n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

max_prime = -1

# tìm số nguyên tố lớn nhất
for i in range(n):
    for j in range(m):
        if is_prime(A[i][j]):
            if A[i][j] > max_prime:
                max_prime = A[i][j]

# output
if max_prime == -1:
    print("NOT FOUND")
else:
    print(max_prime)
    for i in range(n):
        for j in range(m):
            if A[i][j] == max_prime:
                print(f"Vi tri [{i}][{j}]")