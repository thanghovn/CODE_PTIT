t = int(input())

for _ in range(t):
    s = input()
    MIN = 10**9
    n = 0
    ok = False

    for char in s:
        if char.isdigit():
            n = n*10 + int(char)
            ok = True
        else:
            if ok:
                MIN = min(MIN, n)
                n = 0
                ok = False

    if ok:
        MIN = min(MIN, n)

    print(MIN)
