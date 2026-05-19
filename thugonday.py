n = int(input())
a=list(map(int, input().split()))
st=[]

for x in a:
    if st and (st[-1] + x) % 2 == 0:
        st.pop()
    else:
        st.append(x)

print(len(st))