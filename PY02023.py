def digit_sum(x):
    return sum(int(d) for d in str(x))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a_sorted = sorted(a, key=lambda x: (digit_sum(x), x))

    print(*a_sorted)
