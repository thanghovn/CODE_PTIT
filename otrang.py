import math

INF = 10**18

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = {}  # dp[g] = chi phí nhỏ nhất để có gcd = g

    for i in range(n):
        ndp = dict(dp)  # copy dp cũ

        # Trường hợp chỉ dùng thẻ i
        g = a[i]
        cost = c[i]
        if g not in ndp or ndp[g] > cost:
            ndp[g] = cost

        # Ghép thẻ i với các trạng thái cũ
        for g_old, cost_old in dp.items():
            g_new = math.gcd(g_old, a[i])
            new_cost = cost_old + c[i]
            if g_new not in ndp or ndp[g_new] > new_cost:
                ndp[g_new] = new_cost

        dp = ndp

    # Kết quả
    if 1 in dp:
        print(dp[1])
    else:
        print(-1)
