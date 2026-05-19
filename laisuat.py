t = int(input())
for i in range(t):
    n = float(input())
    x = float(input())
    m = float(input())
    cnt = 1
    while True:
        n += (n * x) / 100
        if n >= m :
            break
        cnt += 1
    print (cnt)