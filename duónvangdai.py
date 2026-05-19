# Nhập dữ liệu
m = int(input("Nhập m (độ dài đường vành đai): "))
v = int(input("Nhập v (vận tốc km/giờ): "))
t = int(input("Nhập t (thời gian giờ): "))
d = input("Nhập d (A - thuận, C - ngược): ")

# Quãng đường đi được
s = v * t

# Xác định vị trí dừng
if d == 'A':
    result = s % m
if d == 'C' :
    result = (-s) % m

# In kết quả
print("Result =", result)
