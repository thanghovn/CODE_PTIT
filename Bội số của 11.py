while True:
    x = input().strip()
    if x == "-1":
        break

    if int(x) % 11 == 0:
        print('YES')
    else :
        print('NO')