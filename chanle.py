t = int(input())
for i in range(t):
    n = input().strip()
    ok = True
    a= len(n)
    for j in range(1,a):
        if abs(int(n[j]) - int(n[j-1])) != 2:
            ok= False
            break
    x = int(n)
    sum = 0

    while x > 0:
        sum = sum + x%10
        x //= 10
    if ok and sum % 10 == 0:
        print('YES')
    else:
        print('NO')

