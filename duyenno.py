t = int(input())
for _ in range(t):
    num = input().strip()
    if num[0] == num[-1]:
        print('YES')
    else:
        print('NO')