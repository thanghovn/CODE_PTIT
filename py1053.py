t = int(input())
for _ in range(t):
    s = input().strip()

    tong = 0
    for c in s:
        tong += int(c)

    if tong % 3 == 0:
        print("YES")
    else:
        print("NO")
