digits = ['2', '3', '5', '7']
n = int(input())

res = []


def backtrack(s, mask):
    if len(s) >= 4:
        # đủ 4 số (mask = 1111 = 15)
        if mask == 15 and s[-1] != '2':
            res.append(s)

    if len(s) == n:
        return

    for i in range(4):
        backtrack(s + digits[i], mask | (1 << i))


backtrack("", 0)

# sắp xếp tăng dần
res.sort(key=lambda x: (len(x), x))

for x in res:
    print(x)