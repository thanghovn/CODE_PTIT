n = int(input())

stack = []
ans = 0

for _ in range(n):
    x = int(input())

    cnt = 1

    while stack and stack[-1][0] < x:
        ans += stack[-1][1]
        stack.pop()

    if stack and stack[-1][0] == x:
        c = stack[-1][1]
        ans += c
        stack.pop()

        cnt = c + 1

        if stack:
            ans += 1

        stack.append((x, cnt))

    else:
        if stack:
            ans += 1

        stack.append((x, cnt))

print(ans)