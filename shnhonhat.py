n = int(input())
a = list(map(int, input().split()))

a.sort()

missing = 1

for x in a:
    if x == missing:
        missing += 1

print(missing)
