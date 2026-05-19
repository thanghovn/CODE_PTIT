s1 = input().lower().split()
s2 = input().lower().split()

set1 = set(s1)
set2 = set(s2)

# giao
giao = sorted(set1 & set2)

# hợp
hop = sorted(set1 | set2)

print(" ".join(hop))
print(" ".join(giao))
