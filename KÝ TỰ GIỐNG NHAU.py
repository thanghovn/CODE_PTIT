import heapq

T = int(input())

for _ in range(T):
    N = int(input())
    X, Y, Z = map(int, input().split())

    limit = 2 * N + 5
    INF = 10**18

    dist = [INF] * (limit + 1)
    dist[0] = 0

    pq = [(0, 0)]

    while pq:
        cost, u = heapq.heappop(pq)

        if cost != dist[u]:
            continue

        if u == N:
            break

        # insert
        if u + 1 <= limit:
            v = u + 1
            if dist[v] > cost + X:
                dist[v] = cost + X
                heapq.heappush(pq, (dist[v], v))

        # delete
        if u - 1 >= 0:
            v = u - 1
            if dist[v] > cost + Y:
                dist[v] = cost + Y
                heapq.heappush(pq, (dist[v], v))

        # copy
        if u > 0 and u * 2 <= limit:
            v = u * 2
            if dist[v] > cost + Z:
                dist[v] = cost + Z
                heapq.heappush(pq, (dist[v], v))

    print(dist[N])