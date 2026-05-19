n = int(input())

priority = {
    '1': 2.0,
    '2': 1.5,
    '3': 1.0,
    '4': 0.0
}

subject = {
    'A': 'TOAN',
    'B': 'LY',
    'C': 'HOA'
}

ds = []

for i in range(1, n + 1):
    name = input().strip()
    ma_xt = input().strip()
    tin = float(input())
    chuyen_mon = float(input())

    ma_gv = f"GV{i:02d}"

    mon = subject[ma_xt[0]]
    diem_ut = priority[ma_xt[1]]

    tong = tin * 2 + chuyen_mon + diem_ut

    if tong >= 18:
        ket_qua = "TRUNG TUYEN"
    else:
        ket_qua = "LOAI"

    ds.append([ma_gv, name, mon, tong, ket_qua])

ds.sort(key=lambda x: -x[3])

for gv in ds:
    print(gv[0], gv[1], gv[2], f"{gv[3]:.1f}", gv[4])