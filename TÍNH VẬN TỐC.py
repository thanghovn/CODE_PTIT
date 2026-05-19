from datetime import datetime

class vantoc:
    def __init__(self, name, donvi,ve):
        self.name = name
        self.donvi = donvi

        ma_dv= ''.join([x[0]for x in donvi.split()])
        ma_ten=''.join([x[0]for x in name.split()])
        self.ma = (ma_dv+ma_ten).upper()

        start = datetime.strptime("6:00", "%H:%M")
        end = datetime.strptime(ve, "%H:%M")

        t = (end - start).total_seconds()/3600
        self.v = 120 / t

    def __str__(self):
        return f"{self.ma} {self.name} {self.donvi} {round(self.v)} Km/h"

n = int(input())
ds = []

for _ in range(n):
    ten = input()
    donvi = input()
    tg = input()
    ds.append(vantoc(ten,donvi,tg))

ds.sort(key=lambda x : x.v, reverse=True)

for i in ds:
    print(i)