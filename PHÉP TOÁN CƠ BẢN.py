def match(pattern, value):
    value = str(value)
    if len(value) != len(pattern):
        return False
    for p, v in zip(pattern, value):
        if p != '?' and p != v:
            return False
    return True


ops = ['+', '-', '*', '/']

for _ in range(int(input())):
    s = input().strip()

    a = s[0:2]
    op = s[3]
    b = s[5:7]
    c = s[10:12]

    found = False

    for x in range(10, 100):
        if not match(a, x):
            continue
        for y in range(10, 100):
            if not match(b, y):
                continue

            for o in ops:
                # kiểm tra phép toán có khớp không
                if op != '?' and op != o:
                    continue

                if o == '+':
                    z = x + y
                elif o == '-':
                    z = x - y
                elif o == '*':
                    z = x * y
                elif o == '/':
                    if y == 0 or x % y != 0:
                        continue
                    z = x // y

                if z < 10 or z > 99:
                    continue

                if not match(c, z):
                    continue

                print(f"{x} {o} {y} = {z}")
                found = True
                break
            if found:
                break
        if found:
            break

    if not found:
        print("WRONG PROBLEM!")