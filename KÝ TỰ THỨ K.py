def find_char(n ,k):
    if n == 1 :
        return 'A'
    mid = 2**(n-1)

    if k == mid :
        return chr(ord('A') + n-1)
    elif k < mid :
        return find_char(n-1,k)
    else :
        return find_char(n-1,k-mid)

for _ in range(int(input())):
    n ,k = map(int,input().split())
    print(find_char(n,k))