def to_base4(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n % 4) + s
        n //= 4
    return s

t = int(input())

for _ in range(t):
    b = int(input())
    x = input().strip()

    val = int(x, 2)

    if b == 2:
        print(x)

    elif b == 4:
        print(to_base4(val))

    elif b == 8:
        print(oct(val)[2:])

    elif b == 16:
        print(hex(val)[2:].upper())