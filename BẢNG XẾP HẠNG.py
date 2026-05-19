class sinhvien:
    def __init__(self,name,correct,submit):
        self.name = name.strip()
        self.correct= correct
        self.submit= submit
    def __lt__(self,other):
        if self.correct != other.correct:
            return self.correct > other.correct
        if self.submit != other.submit:
            return self.submit < other.submit
    def __str__(self):
        return f"{self.name} {self.correct} {self.submit}"

n = int(input())
ds= []
for i in range(n):
    name= input()
    correct, submit= input().split()
    ds.append(sinhvien(name,correct,submit))
ds.sort()
for sv in ds:
    print(sv)