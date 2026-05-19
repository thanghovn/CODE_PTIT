T = int(input())

for _ in range(T):
    s = input()

    stack = []
    cnt = 0
    ans = []

    for c in s:
        if c == '(':
            cnt += 1
            stack.append(cnt)
            ans.append(cnt)

        elif c == ')':
            ans.append(stack[-1])
            stack.pop()

    print(*ans)