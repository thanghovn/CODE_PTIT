def xuli(char):
    cnt=1

    for i in range(0,len(char)):
        if i < len(char) - 1 and char[i] == char[i + 1]:
            cnt += 1
        else :
            print(cnt,end='')
            print(char[i],end='')
            cnt=1

t = int(input())
for i in range(t):
    char = input()
    xuli(char)
    print()

#aaabbcc
#n=6
#i=5 char[6]
