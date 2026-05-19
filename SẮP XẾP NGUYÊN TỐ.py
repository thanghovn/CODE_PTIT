# tạo bảng nguyên tố bằng sàng
prime = [True] * 1001
prime[0] = prime[1] = False

for i in range(2, int(1000**0.5) + 1):
    if prime[i]:
        for j in range(i*i, 1001, i):
            prime[j] = False

# input
n = int(input())
a = list(map(int, input().split()))

# lấy các số nguyên tố
p = [x for x in a if prime[x]]

# sort
p.sort()

# thay lại
idx = 0
for i in range(n):
    if prime[a[i]]:
        a[i] = p[idx]
        idx += 1

# output
print(*a)