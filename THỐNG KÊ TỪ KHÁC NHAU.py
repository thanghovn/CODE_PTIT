import re
from collections import Counter

n = int(input())

cnt = Counter()

for _ in range(n):
    s = input().lower()

    s = re.sub(r"[,.?!:;()\-/]", " ", s)

    words = s.split()

    cnt.update(words)

ans = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

for word, freq in ans:
    print(word, freq)