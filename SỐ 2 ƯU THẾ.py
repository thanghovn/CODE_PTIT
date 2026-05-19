from collections import deque


def check(s):
    return s.count('2') > len(s) // 2


def solve(n):
    q = deque()
    q.append("1")
    q.append("2")

    res = []

    while len(res) < n:
        s = q.popleft()

        if check(s):
            res.append(s)

        q.append(s + "0")
        q.append(s + "1")
        q.append(s + "2")

    return res


# Input
t = int(input())
for _ in range(t):
    n = int(input())
    ans = solve(n)
    print(*ans)