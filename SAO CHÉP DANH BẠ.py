class danhba:
    def __init__(self, name, so, ngay):
        self.name = name
        self.so = so
        self.ngay = ngay

    def __str__(self):
        return f"{self.name}: {self.so} {self.ngay}"

def main():
    ds = []
    file = open("SOTAY.txt", "r")
    inp = file.read().split('\n')

    while len(inp) > 0:
        tmp = inp[0]
        inp.pop(0)

        if tmp[:4] == 'Ngay':
            ngay = tmp.split()[1]
        elif len(inp) > 0:
            sdt = inp[0]
            inp.pop(0)
            ds.append(danhba(tmp, sdt, ngay))
    ds.sort(key=lambda x: (x.name.split()[-1],x.name))
    file.close()
    ot = open('DIENTHOAI.txt', 'w')
    for i in ds:
        ot.write(str(i) + '\n')
    ot.close()

if __name__ == "__main__":
    main()