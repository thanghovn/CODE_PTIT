import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input().strip()

    # lấy 4 chữ số cuối (hoặc toàn bộ nếu < 4 chữ số)
    last4 = s[-4:]
    x = int(last4)

    if is_prime(x):
        print("YES")
    else:
        print("NO")
