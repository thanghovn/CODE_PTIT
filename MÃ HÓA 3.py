def value(c):
    return ord(c) - ord('A')


def rotate_char(c, k):
    return chr((value(c) + k) % 26 + ord('A'))


def rotate_string(s):
    k = sum(value(c) for c in s)
    res = ""

    for c in s:
        res += rotate_char(c, k)

    return res


def merge(a, b):
    res = ""

    for i in range(len(a)):
        k = value(b[i])
        res += rotate_char(a[i], k)

    return res


t = int(input())

for _ in range(t):
    s = input().strip()

    mid = len(s) // 2

    left = s[:mid]
    right = s[mid:]

    left = rotate_string(left)
    right = rotate_string(right)

    print(merge(left, right))