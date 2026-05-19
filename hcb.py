n = int(input())

mx1 = -10**18
mx2 = -10**18

for _ in range(n):
    x = int(input())
    if x > mx1:
        mx2 = mx1
        mx1 = x
    elif x > mx2:
        mx2 = x

print(f"Silver = {mx2}")
