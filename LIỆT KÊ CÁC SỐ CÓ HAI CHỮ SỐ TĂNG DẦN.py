s = str(input())
ket_qua=set()
for i in range(0,len(s)-1,2):
    so = int(s[i:i+2])
    ket_qua.add(so)

ds_sx=sorted(list(ket_qua))
print(*(ds_sx))