def check(n) :
    leap = True
    while n > 0 :
        val = n % 10
        if(val != 4 and val != 7) :
            leap = False
        n //= 10
    return leap

t = int(input())
for i in range(t):
    N = int(input())
    if (check(N)):
        print('YES')
    else :
        print('NO')