import sys

def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def main():
    data = sys.stdin
    t = int(data.readline())

    for _ in range(t):
        n, d = map(int, data.readline().split())
        a = list(map(int, data.readline().split()))

        d %= n

        # đảo [0..d-1]
        reverse(a, 0, d - 1)
        # đảo [d..n-1]
        reverse(a, d, n - 1)
        # đảo toàn bộ
        reverse(a, 0, n - 1)

        print(*a)

if __name__ == "__main__":
    main()
