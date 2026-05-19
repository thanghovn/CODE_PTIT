while(True):
    n=int(input())
    if n==0:
        break
    else :
        cnt = 1
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                cnt += 1
            else:
                n = n * 3 + 1
                cnt += 1
        print(cnt)