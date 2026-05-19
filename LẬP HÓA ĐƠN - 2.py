from datetime import datetime
class Khachhang :
    def __init__(self, ma, ten, phong, nhan, tra, dv) :
        self.ma = ma
        self.ten = ten.strip()
        self.phong = phong.strip()

        d1 = datetime.strptime(nhan.strip(), '%d/%m/%Y')
        d2 = datetime.strptime(tra.strip(), '%d/%m/%Y')

        self.songay = (d2-d1).days+1

        tang = int(phong[0])
        gia = {1:25, 2:34, 3:50, 4:80}

        self.tien = self.songay * gia[tang] + dv
    def __str__(self):
        return f"{self.ma} {self.ten} {self.phong} {self.songay} {self.tien}"

n = int(input())
ds = []
for i in range(1,n+1):
    ten = input()
    phong = input()
    nhan = input()
    tra = input()
    dv =int(input())
    ma = "KH{:02d}".format(i)
    ds.append(Khachhang(ma, ten, phong, nhan, tra, dv))
ds.sort(key=lambda x: x.tien,reverse=True)
for x in ds :
    print(x)