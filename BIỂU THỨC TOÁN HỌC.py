import sys


def solve():
    # Đọc dữ liệu N và K
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        n, k = map(int, line1)

        # Đọc dãy số a
        a = []
        while len(a) < n:
            a.extend(map(int, sys.stdin.readline().split()))
    except ValueError:
        return

    target = 5 * k
    # Hệ số tương ứng với vị trí j (1-indexed)
    # j % 5 sẽ cho các giá trị: 1, 2, 3, 4, 0
    coeffs = {1: 1, 2: -2, 3: 3, 4: -4, 0: 5}

    # Khởi tạo mảng DP với giá trị vô cùng bé
    # dp[j] là giá trị lớn nhất khi đã chọn được j phần tử
    dp = [-float('inf')] * (target + 1)
    dp[0] = 0

    for x in a:
        # Duyệt ngược từ target về 1 để tránh việc một phần tử a[i]
        # bị sử dụng nhiều lần trong cùng một lượt cập nhật (DP tối ưu bộ nhớ)
        for j in range(target, 0, -1):
            coeff = coeffs[j % 5]
            # Cập nhật nếu việc chọn x mang lại giá trị tốt hơn
            if dp[j - 1] != -float('inf'):
                dp[j] = max(dp[j], dp[j - 1] + x * coeff)

    print(dp[target])


def main():
    line = sys.stdin.readline()
    if line:
        t = int(line.strip())
        for _ in range(t):
            solve()


if __name__ == "__main__":
    main()