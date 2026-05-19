class thi_sinh:
    def __init__(self, ten, sinh, diem1, diem2, diem3):
        self.ten = ten
        self.sinh = sinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3

    def tong(self):
        tong = self.diem1 + self.diem2 + self.diem3
        return tong

    def out(self):
        print(f"{self.ten} {self.sinh} {self.tong()}")

def main():
    ten = str(input())
    sinh = str(input())
    diem1 = float(input())
    diem2 = float(input())
    diem3 = float(input())
    a = thi_sinh(ten, sinh, diem1, diem2, diem3)
    a.out()

main()