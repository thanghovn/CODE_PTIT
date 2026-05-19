n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

def is_palindrome(n):
    return n >= 10 and str(n) == str(n)[::-1]

max_palin = -1

# tìm số thuận nghịch lớn nhất
for i in range(n):
    for j in range(m):
        if is_palindrome(A[i][j]):
            if A[i][j] > max_palin:
                max_palin = A[i][j]

# in kết quả
if max_palin == -1:
    print("NOT FOUND")
else:
    print(max_palin)
    for i in range(n):
        for j in range(m):
            if A[i][j] == max_palin:
                print(f"Vi tri [{i}][{j}]")