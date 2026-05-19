def rotation_steps(s, target):
    t = s
    for i in range(len(s)):
        if t == target:
            return i
        t = t[1:] + t[0]
    return -1


while True:
    try:
        n = int(input())
        arr = [input().strip() for _ in range(n)]

        m = len(arr[0])
        ans = float('inf')

        base = arr[0]

        for i in range(m):
            target = base[i:] + base[:i]
            total = i
            ok = True

            for j in range(1, n):
                step = rotation_steps(arr[j], target)
                if step == -1:
                    ok = False
                    break
                total += step

            if ok:
                ans = min(ans, total)

        if ans == float('inf'):
            print("NO")
        else:
            print(ans)

    except:
        break