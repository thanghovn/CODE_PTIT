import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m, L = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    pre = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            pre[i + 1][j + 1] = (
                pre[i][j + 1]
                + pre[i + 1][j]
                - pre[i][j]
                + a[i][j]
            )

    for i in range(n - L + 1):
        row = []
        for j in range(m - L + 1):
            x1, y1 = i, j
            x2, y2 = i + L - 1, j + L - 1

            total = (
                pre[x2 + 1][y2 + 1]
                - pre[x1][y2 + 1]
                - pre[x2 + 1][y1]
                + pre[x1][y1]
            )

            row.append(total // (L * L))

        print(*row)