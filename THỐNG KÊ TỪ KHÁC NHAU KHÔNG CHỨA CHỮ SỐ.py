import re
from collections import Counter

n = int(input())

cnt = Counter()

for _ in range(n):
    s = input().lower()

    # thay dấu câu bằng khoảng trắng
    s = re.sub(r"[,.?!:;()\-/]", " ", s)

    # xóa toàn bộ chữ số
    s = re.sub(r"[0-9]", "", s)

    cnt.update(s.split())

ans = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

for word, freq in ans:
    print(word, freq)