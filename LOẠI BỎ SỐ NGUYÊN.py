def is_int(s):
    try:
        int(s)
        return True
    except:
        return False


with open("DATA.in", "r") as f:
    a = f.read().split()

res = []

for x in a:
    if not is_int(x):
        res.append(x)

res.sort()

print(*res)