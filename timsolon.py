t = int(input())

for _ in range(t):
    s = input()
    MAX = -1
    n = 0
    ok = False

    for char in s:
        if char.isdigit():
            n = n*10 + int(char)
            ok = True
        else:
            if ok:
                MAX = max(MAX, n)
                n = 0
                ok = False

    if ok:
        MAX = max(MAX, n)

    print(MAX)
