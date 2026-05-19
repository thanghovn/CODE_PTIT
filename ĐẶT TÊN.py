n, k = map(int, input().split())
names = input().split()

names = sorted(set(names))

res=[]
comb=[]

def backtrack(s):
    if len(comb)==k:
        print(*comb)
        return
    for i in range(s,len(names)):
        comb.append(names[i])
        backtrack(i+1)
        comb.pop()
backtrack(0)