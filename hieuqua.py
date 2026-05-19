a0, b0, c0 = map(int, input().split())
a1, b1, c1 = map(int, input().split())

t0 = a0*3600 + b0*60 + c0
t1 = a1*3600 + b1*60 + c1

if t1 < t0:
    t1 += 24*3600

print(t1 - t0)
