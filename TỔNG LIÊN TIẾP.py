import sys


def solve():
    line = sys.stdin.readline()
    if not line:
        return
    try:
        n = int(line.strip())
    except ValueError:
        return

    count = 0
    # k là số lượng các số hạng liên tiếp (k >= 2)
    # Tổng nhỏ nhất của k số là k*(k+1)/2
    # Do đó k*(k+1)/2 <= n
    k = 2
    while k * (k + 1) // 2 <= n:
        # Tử số của biểu thức tính 2x
        numerator = 2 * n - k ** 2 + k
        # Kiểm tra x có phải số nguyên dương không
        if numerator > 0 and numerator % (2 * k) == 0:
            count += 1
        k += 1

    print(count)


line = sys.stdin.readline()
if line:
    t_str = line.strip()
    if t_str:
        t = int(t_str)
        for _ in range(t):
            solve()