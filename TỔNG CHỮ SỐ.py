n= input().strip()
turn= 0
while True:
    turn+=1
    s=0
    for c in n:
        if c != "-":
            s += int(c)
    n=str(s)
    if len(n)==1:
        break
print(turn)