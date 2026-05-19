from datetime import datetime

class tram_do:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten
        self.time = 0
        self.luong = 0

    def trung_binh(self):
        return self.luong /self.time*60

    def add (self, start, end, luong):
        d = datetime.strptime(start, "%H:%M")
        c = datetime.strptime(end, "%H:%M")
        t = (c - d).total_seconds()/60
        self.time += t
        self.luong += luong
    def __str__(self):
        return f"{self.ma} {self.ten} {self.trung_binh():.2f}"

def main():
    n = int(input())
    ds = []
    mp = {}
    cnt = 1
    for _ in range(n):
        ten = input()
        start = input()
        end = input()
        luong = float(input())
        if ten not in mp:
            ma = f"T{cnt:02d}"
            mp[ten] = tram_do(ma, ten)
            ds.append(mp[ten])
            cnt += 1
        mp[ten].add(start, end, luong)

    for x in ds:
        print(x)

if __name__ == '__main__':
    main()