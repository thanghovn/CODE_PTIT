def daochu(string):
    return string[::-1]

t = int(input())
for i in range(t):
    s1 = input().strip()
    s2 = daochu(s1)
    n=len(s1)

    leap = True
    for j in range(1,n):
        if abs(ord(s1[j]) - ord(s1[j-1])) != abs(ord(s2[j]) - ord(s2[j-1])):
            leap = False
            break

    if leap:
        print('YES')
    else :
        print('NO')
