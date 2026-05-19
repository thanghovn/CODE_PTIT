t = int(input())
for i in range(t):
    n = input()
    sum = 0
    mul=1
    ok = False
    for j in range(len(n)):
        if j % 2 == 1:
            sum += int(n[j])
        else :
            if int(n[j]) != 0:
                ok = True
                mul *= int(n[j])
    print(f"{mul} {sum if ok else 0}")
