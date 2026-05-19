def hamming_index(n):
    cnt = 0
    a = 1
    while a <= n:
        b = a
        while b <= n:
            c = b
            while c <= n:
                cnt += 1
                c *= 5
            b *= 3
        a *= 2
    return cnt


t=int(input())
for i in range(t):
    val = int(input())
    if hamming_index(val):
        print(val)
    else :
        print('Not in sequence')