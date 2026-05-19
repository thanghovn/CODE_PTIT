for t in range(1,int(input())+1):
    s1=input().strip()
    s2=input().strip()
    if len(s1) != len(s2):
        print(f"Test {t}: NO")
        continue

    cnt= {}
    for c in s1:
        cnt[c]= cnt.get(c,0)+1

    for c in s2:
        if c not in cnt:
            print(f"Test {t}: NO")
            break
        cnt[c]= cnt[c]-1
        if cnt[c] < 0:
            print(f"Test {t}: NO")
            break
    else :
            print(f"Test {t}: YES")