s = str(input())
while len(s) > 1:
    n= len(s)
    mid= n//2
    sum= int(s[:mid]) + int(s[mid:])
    print(sum)
    s=str(sum)