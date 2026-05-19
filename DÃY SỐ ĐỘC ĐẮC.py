import sys

# Tăng giới hạn đệ quy nhưng vừa phải để tránh tốn stack memory
sys.setrecursionlimit(10 ** 5)


def is_unique(idx, l, r, prev_p, next_p):
    # Một phần tử là duy nhất trong đoạn [l, r] nếu:
    # Vị trí xuất hiện trước đó nằm ngoài l và vị trí kế tiếp nằm ngoài r
    return prev_p[idx] < l and next_p[idx] > r


def check(l, r, prev_p, next_p):
    if l >= r:
        return True

    # Tìm từ hai đầu vào giữa
    for i in range((r - l) // 2 + 1):
        # Kiểm tra từ bên trái
        if is_unique(l + i, l, r, prev_p, next_p):
            return check(l, l + i - 1, prev_p, next_p) and check(l + i + 1, r, prev_p, next_p)

        # Kiểm tra từ bên phải
        if is_unique(r - i, l, r, prev_p, next_p):
            return check(l, r - i - 1, prev_p, next_p) and check(r - i + 1, r, prev_p, next_p)

    return False


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    t = int(input_data[idx])
    idx += 1

    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = input_data[idx: idx + n]
        idx += n

        # Tiền xử lý vị trí để check O(1)
        prev_p = [-1] * n
        next_p = [n] * n
        last_seen = {}

        # Điền prev_p
        for i in range(n):
            val = a[i]
            if val in last_seen:
                prev_p[i] = last_seen[val]
            last_seen[val] = i

        # Điền next_p
        last_seen.clear()
        for i in range(n - 1, -1, -1):
            val = a[i]
            if val in last_seen:
                next_p[i] = last_seen[val]
            last_seen[val] = i

        if check(0, n - 1, prev_p, next_p):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()