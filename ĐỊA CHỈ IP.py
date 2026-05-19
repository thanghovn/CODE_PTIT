for _ in range(int(input())):
    try :
        a = list(map(int, input().split('.')))
    except Exception as e :
        print('NO')
        continue

    Max = max(a)
    Min = min(a)
    if Min < 0 or Max > 255 or len(a) != 4 :
        print('NO')
    else :
        print('YES')