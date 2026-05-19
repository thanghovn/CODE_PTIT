s = set()

while len(s) < 10:
    nums = list(map(int, input().split()))
    for x in nums:
        s.add(x % 42)

print(len(s))
