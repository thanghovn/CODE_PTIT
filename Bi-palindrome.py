def convert_base(x, base):
    if x == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJ"
    res = ""

    while x > 0:
        res += digits[x % base]
        x //= base

    return res[::-1]


def is_palindrome(s):
    return s == s[::-1]


while True:
    line = input().strip()
    if line == "-1":
        break

    x, a, b = map(int, line.split())

    sa = convert_base(x, a)
    sb = convert_base(x, b)

    if is_palindrome(sa) and is_palindrome(sb):
        print("YES")
    else:
        print("NO")