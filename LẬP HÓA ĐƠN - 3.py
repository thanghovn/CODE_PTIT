class Khachhang:
    def __init__(self, ma, ten, soluong, gia, chietkhau):
        self.ma = ma
        self.ten = ten
        self.soluong = soluong
        self.gia = gia
        self.chietkhau = chietkhau

    def thanhtoan(self):
        tongtien = self.gia * self.soluong - self.chietkhau
        return tongtien

    def __str__(self):
        return f"{self.ma} {self.ten} {self.soluong} {self.gia} {self.chietkhau} {self.thanhtoan()}"

def main():
    ds = []
    for _ in range(int(input())):
        ma = input()
        ten = input()
        soluong = int(input())
        gia = int(input())
        chietkhau = int(input())
        ds.append(Khachhang(ma, ten, soluong, gia, chietkhau))
        ds.sort(key=lambda x: x.thanhtoan(), reverse=True)
    for kh in ds:
        print(kh)

if __name__ == '__main__':
    main()