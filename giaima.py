def xuli(c):
    al = ''
    for char in c:
        if char.isalpha():
            al = char
        if char.isdigit():
            for i in range(int(char)):
                print(al,end='')
    print()


for i in range(int(input())):
    c = input()
    xuli(c)