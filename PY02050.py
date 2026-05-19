t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    stack = []
    res = []

    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()

        if not stack:
            res.append(i + 1)
        else:
            res.append(i - stack[-1])

        stack.append(i)

    print(*res)