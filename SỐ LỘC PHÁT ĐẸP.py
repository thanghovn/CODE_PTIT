n = input().strip()
i = 0
ok = True

while i < len(n):
    if n[i:i+3] == "688":
        i += 3
    elif n[i:i+2] == "68":
        i += 2
    elif n[i] == "6":
        i += 1
    else:
        ok = False
        break

print("YES" if ok else "NO")