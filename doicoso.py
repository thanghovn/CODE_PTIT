t = int(input())
f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(t):
    n,b = map(int,input().split())
    s=''
    while n>0:
        x= n % b
        s += f[x]
        n //= b
    print(s[::-1])
