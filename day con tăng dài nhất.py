import math
import sys


def solve():
    # Đọc N và K
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        n, k = map(int, line1)

        # Đọc mảng A
        a = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return

    min_len = float('inf')

    for i in range(n):
        # Nếu phần tử hiện tại không chia hết cho K, chắc chắn dãy chứa nó không có GCD = K
        if a[i] % k != 0:
            continue

        current_gcd = a[i]

        # Nếu ngay phần tử đầu tiên đã bằng K
        if current_gcd == k:
            min_len = min(min_len, 1)
            if min_len == 1: break  # Không thể ngắn hơn 1, thoát sớm cho nhanh
            continue

        for j in range(i + 1, n):
            # Nếu gặp số không chia hết cho K, ngắt luôn dãy con này
            if a[j] % k != 0:
                break

            current_gcd = math.gcd(current_gcd, a[j])

            # Nếu GCD đã đạt bằng K, cập nhật độ dài và chuyển sang i tiếp theo
            if current_gcd == k:
                min_len = min(min_len, j - i + 1)
                break

            # Nếu GCD nhỏ hơn K, không thể tăng lại được nữa (tính chất của GCD)
            if current_gcd < k:
                break

        if min_len == 1: break

    if min_len == float('inf'):
        print("-1")
    else:
        print(min_len)


def main():
    line = sys.stdin.readline()
    if line:
        t = int(line)
        for _ in range(t):
            solve()


if __name__ == "__main__":
    main()