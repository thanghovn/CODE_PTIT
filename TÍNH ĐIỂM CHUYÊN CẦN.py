class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem = 10
        self.ghichu = ""

    def tinh_diem(self, s):
        vang = s.count('v')
        muon = s.count('m')

        self.diem = 10 - (vang*2 + muon)

        if self.diem < 0:
            self.diem = 0

        if self.diem == 0:
            self.ghichu = "KDDK"

    def __str__(self):
        if self.ghichu:
            return f"{self.ma} {self.ten} {self.lop} {self.diem} {self.ghichu}"
        return f"{self.ma} {self.ten} {self.lop} {self.diem}"


n = int(input())
ds = []

for i in range(n):
    ma = input().strip()
    ten = input().strip()
    lop = input().strip()
    ds.append(SinhVien(ma, ten, lop))

for i in range(n):
    line = input().split()
    ma = line[0]
    s = line[1]

    for sv in ds:
        if sv.ma == ma:
            sv.tinh_diem(s)
            break

for sv in ds:
    print(sv)