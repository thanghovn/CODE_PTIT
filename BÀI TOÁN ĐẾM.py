n = int(input())
a = list(map(int, input().split()))

s = set(a)
missing = []

for i in range(1, a[-1] + 1):
    if i not in s:
        missing.append(i)

if not missing:
    print("Excellent!")
else:
    for x in missing:
        print(x)