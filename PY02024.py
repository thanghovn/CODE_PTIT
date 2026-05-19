import math

def digit_product(x):
    return math.prod(int(d) for d in str(x))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a_sorted = sorted(a, key=lambda x: (digit_product(x), x))

    print(*a_sorted)
