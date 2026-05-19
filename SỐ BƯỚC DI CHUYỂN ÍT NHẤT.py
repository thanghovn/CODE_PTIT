import sys
import heapq

INF = 10**18

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    dist = [[INF] * m for _ in range(n)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]

    while pq:
        cost, i, j = heapq.heappop(pq)

        if cost != dist[i][j]:
            continue

        if i == n - 1 and j == m - 1:
            break

        # đi xuống
        if i + 1 < n:
            w = abs(a[i][j] - a[i + 1][j])
            if dist[i + 1][j] > cost + w:
                dist[i + 1][j] = cost + w
                heapq.heappush(pq, (dist[i + 1][j], i + 1, j))

        # đi sang phải
        if j + 1 < m:
            w = abs(a[i][j] - a[i][j + 1])
            if dist[i][j + 1] > cost + w:
                dist[i][j + 1] = cost + w
                heapq.heappush(pq, (dist[i][j + 1], i, j + 1))

        # đi chéo xuống phải
        if i + 1 < n and j + 1 < m:
            w = abs(a[i][j] - a[i + 1][j + 1])
            if dist[i + 1][j + 1] > cost + w:
                dist[i + 1][j + 1] = cost + w
                heapq.heappush(pq, (dist[i + 1][j + 1], i + 1, j + 1))

    print(dist[n - 1][m - 1])