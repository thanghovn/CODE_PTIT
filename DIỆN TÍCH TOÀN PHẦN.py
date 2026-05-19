import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    t = int(input_data[ptr])
    ptr += 1

    for _ in range(t):
        m = int(input_data[ptr])
        n = int(input_data[ptr + 1])
        ptr += 2

        # Khởi tạo ma trận chiều cao với viền bằng 0 để dễ tính toán
        h = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                h[i][j] = int(input_data[ptr])
                ptr += 1

        total_area = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if h[i][j] > 0:
                    # Mặt đỉnh và mặt đáy
                    total_area += 2

                    # Xét 4 phía, cộng phần chiều cao chênh lệch
                    # Phía trên
                    total_area += max(0, h[i][j] - h[i - 1][j])
                    # Phía dưới
                    total_area += max(0, h[i][j] - h[i + 1][j])
                    # Phía trái
                    total_area += max(0, h[i][j] - h[i][j - 1])
                    # Phía phải
                    total_area += max(0, h[i][j] - h[i][j + 1])

        print(total_area)


if __name__ == "__main__":
    solve()