import re
from collections import Counter

n, k = map(int, input().split())

cnt = Counter()

for _ in range(n):
    s = input().lower()
    s = re.sub(r"[,.?!:;()\-/]", " ", s)
    cnt.update(s.split())

ans = []

for word, freq in cnt.items():
    if freq >= k:
        ans.append((word, freq))

ans.sort(key=lambda x: (-x[1], x[0]))

for word, freq in ans:
    print(word, freq)