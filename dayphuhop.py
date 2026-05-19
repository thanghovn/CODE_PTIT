t= int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans= True
    for i in range(n):
        if a[i] > b[i]:
            ans = False
            break

    if ans:
        print('YES')
    else :
        print('NO')