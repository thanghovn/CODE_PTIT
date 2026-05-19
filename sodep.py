def is_valid(s):
    if len(s) % 2 != 0:
        return False

    for char in s:
        if char not in '02468':
            return False

    return s == s[::-1]


t = int(input())
for _ in range(t):
    n = int(input())
    for m in range(0, n):
        if is_valid(str(m)):
            print(m, end=' ')
    print()
