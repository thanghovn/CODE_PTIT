t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s =  {}
    for c in a:
        if c in s:
            s[c] += 1
        else:
            s[c] = 1
    max_key = None
    max_value = 0
    for k, v in s.items():
        if v > max_value:
            max_key = k
            max_value = v
    if max_value > n//2:
        print(max_key)
    else :
        print('NO')