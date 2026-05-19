import pickle
from collections import Counter

def check(n):
    s = str(n)
    if len(s) < 2:
        return False
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

with open("DATA1.in","rb") as f:
    a = pickle.load(f)

with open("DATA2.in","rb") as f:
    b = pickle.load(f)

c1 = Counter()
c2 = Counter()

for x in a:
    if check(x):
        c1[x] += 1

for x in b:
    if check(x):
        c2[x] += 1

res = sorted(set(c1.keys()) | set(c2.keys()))

for x in res:
    print(x, c1[x], c2[x])