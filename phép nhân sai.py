def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


while True:
    line = input().strip()
    if line == "-1":
        break

    y, z = map(int, line.split())

    s = sum_digits(y)

    if s == 0:
        print(0)  # trường hợp đặc biệt
    else:
        print(z // s)