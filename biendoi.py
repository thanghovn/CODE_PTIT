while True:
    a = list(map(int, input().split()))

    # điều kiện kết thúc input
    if a == [0, 0, 0, 0]:
        break

    cnt = 0

    # lặp đến khi 4 số bằng nhau
    while not (a[0] == a[1] == a[2] == a[3]):
        b = [0] * 4
        for i in range(4):
            b[i] = abs(a[i] - a[(i + 1) % 4])
        a = b
        cnt += 1

    print(cnt)
