while True:
    x = input().strip()
    if x == "-1":
        break
    s = sum(int(x) for x in str(x))

    k = (9 - s) % 9

    result = str(int(x)+k)

    print(result)