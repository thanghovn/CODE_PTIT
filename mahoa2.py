P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    data = input().split()
    K = int(data[0])
    if K == 0:
        break

    S = data[1]
    encoded = ""

    for ch in S:
        idx = P.index(ch)
        encoded += P[(idx + K) % 28]

    encoded = encoded[::-1]

    print(encoded)
