a = [0]*100
arr = []

def result(n, k):
    for i in range(1, k+1):
        print(arr[a[i]-1], end=" ")
    print()

def hop(i, n, k):
    for j in range(a[i-1]+1, n-k+i+1):
        a[i] = j
        if i == k:
            result(n, k)
        else:
            hop(i+1, n, k)

m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(set(arr))
m = len(arr)

a[0] = 0
hop(1, m, k)
