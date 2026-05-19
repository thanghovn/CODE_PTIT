n = int(input())
arr = list(map(float, input().split()))
minA = min(arr)
maxA = max(arr)
for i in arr:
    if i == minA or i == maxA:
        arr.remove(i)
print(f"{sum(arr) / len(arr):.2f}")