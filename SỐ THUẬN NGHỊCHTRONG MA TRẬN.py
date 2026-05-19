def thuan_nghich(n):
    s = str(n)
    return len(s) >= 2 and s == s[::-1]


n, m = map(int, input().split())

a = []
max_val = -1

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

    for x in row:
        if thuan_nghich(x):
            max_val = max(max_val, x)

if max_val == -1:
    print("NOT FOUND")
else:
    print(max_val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_val:
                print(f"Vi tri [{i}][{j}]")