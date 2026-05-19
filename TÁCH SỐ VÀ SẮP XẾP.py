def normalize(s):
    # bỏ số 0 đầu
    s = s.lstrip('0')
    return s if s != "" else "0"


def cmp_key(x):
    return (len(x), x)


n = int(input())
nums = []

for _ in range(n):
    s = input()
    cur = ""

    for c in s:
        if c.isdigit():
            cur += c
        else:
            if cur:
                nums.append(normalize(cur))
                cur = ""

    if cur:
        nums.append(normalize(cur))

# sắp xếp
nums.sort(key=cmp_key)

# in ra
for num in nums:
    print(num)