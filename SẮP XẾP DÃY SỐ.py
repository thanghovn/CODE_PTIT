for _ in range(int(input())):
    n ,m = map(int, input().split())
    a = list(map(int, input().split()))

    mx = max(a)

    pos = a.index(mx)
    a.insert(pos, m)

    am = []
    duong= []

    for x in a:
        if x < 0 :
            am.append(x)
        else :
            duong.append(x)

    res = am + duong
    print(*res)