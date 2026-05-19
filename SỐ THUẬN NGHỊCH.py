import sys


def is_pal(x, k):
    if x < k:
        return True
    digits = []
    temp = x
    while temp > 0:
        digits.append(temp % k)
        temp //= k

    # Kiểm tra đối xứng
    n = len(digits)
    for i in range(n // 2):
        if digits[i] != digits[n - 1 - i]:
            return False
    return True


def solve():
    # Đọc input nhanh
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    m = int(input_data[2])

    count = 0
    for x in range(a, b + 1):
        if x <= 2:
            # 0, 1, 2 luôn là số thuận nghịch trong mọi cơ số K > x
            count += 1
            continue

        is_ok = True
        # Chỉ cần kiểm tra các cơ số từ 2 đến min(m, x)
        # Vì nếu K > x, x luôn là số thuận nghịch (có 1 chữ số)
        check_limit = min(m, x)

        # Kiểm tra từ cơ số nhỏ đến lớn
        for k in range(2, check_limit + 1):
            if not is_pal(x, k):
                is_ok = False
                break

        if is_ok:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()