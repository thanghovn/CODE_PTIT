def sokogiam(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

t = int(input())
for i in range(t):
    n = str(input())
    if (sokogiam(n)):
        print("YES")
    else :
        print("NO")