import math

eps = 1e-6


def circle_center(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if abs(D) < eps:
        return None

    ux = ((x1 * x1 + y1 * y1) * (y2 - y3) +
          (x2 * x2 + y2 * y2) * (y3 - y1) +
          (x3 * x3 + y3 * y3) * (y1 - y2)) / D

    uy = ((x1 * x1 + y1 * y1) * (x3 - x2) +
          (x2 * x2 + y2 * y2) * (x1 - x3) +
          (x3 * x3 + y3 * y3) * (x2 - x1)) / D

    return ux, uy


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


t = int(input())
for _ in range(t):
    n = int(input())
    K = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    found = False

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                center = circle_center(points[i], points[j], points[k])
                if center is None:
                    continue

                R = dist(center, points[i])

                cnt = 0
                for p in points:
                    d = dist(center, p)
                    if d < R - eps:
                        cnt += 1

                if cnt == K:
                    found = True
                    break

            if found:
                break
        if found:
            break

    print("YES" if found else "NO")