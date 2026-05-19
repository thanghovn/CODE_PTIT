for _ in range(int(input())):
    s = input().strip()

    letters = []
    total = 0

    for c in s:
        if c.isalpha():
            letters.append(c)
        else:
            total += int(c)

    letters.sort()
    print("".join(letters)+str(total))