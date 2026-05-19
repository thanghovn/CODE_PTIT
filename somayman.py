def demso(n) :
    cnt = 0
    while n > 0 :
        val = n % 10
        if val == 4 or val == 7 :
            cnt += 1
        n //= 10
    return cnt

N = int(input())
k = demso(N)
if(k == 4 or k == 7) :
    print('YES')
else :
    print('NO')