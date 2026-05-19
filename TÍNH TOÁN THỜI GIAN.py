from datetime import datetime


class khachhang:
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        d = datetime.strptime(vao, "%H:%M")
        c = datetime.strptime(ra, "%H:%M")
        tg = int((c - d).total_seconds() / 60)
        self.gio=tg//60
        self.phut=tg%60
        self.thoigian = tg

    def __str__(self):
        return f"{self.ma} {self.ten} {self.gio} gio {self.phut} phut"

def main():
    ds = []
    for i in range(1,int(input())+1):
        ma = input()
        ten = input()
        vao = input()
        ra = input()
        ds.append(khachhang(ma, ten, vao, ra))
    ds.sort(key=lambda x:x.thoigian, reverse=True)
    for x in ds:
        print(x)
if __name__ == "__main__":
    main()