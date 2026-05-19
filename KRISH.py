def giaithua(n):
    tich = 1
    for i in range(1, n + 1):
        tich *= i
    return tich

t = int(input())
for _ in range(t):
    n = input().strip()
    tong = 0
    for ch in n:
        tong += giaithua(int(ch))
    if tong == int(n):
        print("Yes")
    else:
        print("No")
