import math

t = int(input())
for i in range(t):
    n = int(input())
    tmp = n
    print('1',end='')
    for j in range(2,int(math.sqrt(tmp))+1):
        if tmp % j == 0:
            cnt = 0
            while (tmp % j == 0):
                cnt += 1
                tmp //= j
            print(f" * {j}^{cnt}", end="")
    if tmp > 1:
        print(f" * {tmp}^1", end="")
    print()