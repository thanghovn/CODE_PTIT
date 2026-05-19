t = int(input())
MAXZ=93

a = [0]*(MAXZ+1)
def fibo(MAXZ):
    a[1]=1
    a[2]=1
    for i in range(3,MAXZ+1):
        a[i]=a[i-1]+a[i-2]

fibo(MAXZ)

for _ in range(t):
    l , r = map(int,input().split())
    for i in range(l,r+1):
        print(a[i],end=" ")
    print()