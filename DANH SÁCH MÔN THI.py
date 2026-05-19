n = int(input())

ds = []

for _ in range(n):
    ma_mon = input().strip()
    ten_mon = input().strip()
    hinh_thuc = input().strip()

    ds.append((ma_mon, ten_mon, hinh_thuc))

ds.sort(key=lambda x: x[0])

for ma_mon, ten_mon, hinh_thuc in ds:
    print(ma_mon, ten_mon, hinh_thuc)