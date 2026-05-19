def round_number(n):
    base = 10

    while n >= base:

        n = (n + base // 2) // base * base
        base *= 10

    return n

t = int(input())
for i in range(t) :
    N = int(input().strip())
    print(round_number(N))