word = str(input())
u = 0
l = 0
for c in word:
    if (c.isupper()) :
        u += 1
    else :
        l += 1

if ( u > l ) :
    print(word.upper())
else :
    print(word.lower())