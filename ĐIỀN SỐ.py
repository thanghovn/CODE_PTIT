for _ in range(int(input())):
    n = int(input())
    a= list(map(int,input().split()))
    l = min(a)
    r = max(a)
    result = 0
    for i in range(l,r+1):
        if i not in a:
            result += 1
    print(result)
