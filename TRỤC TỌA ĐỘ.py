import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    segments = []

    for _ in range(n):
        x1, x2 = map(int, input().split())
        segments.append((x1, x2))

    segments.sort(key=lambda x: x[1])

    ans = 0
    last_end = -1

    for start, end in segments:
        if start >= last_end:
            ans += 1
            last_end = end

    print(ans)