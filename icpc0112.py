def songto(n):
    if n < 2 :
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    ans = [i for i in range(2, n + 1) if songto(i)]
    cnt = 0
    for num in ans:
        if num + 6 > n :
            break
        if songto(num + 2) and songto(num + 6):
            cnt += 1
        if songto(num + 4) and songto(num + 6):
            cnt += 1
    print(cnt)