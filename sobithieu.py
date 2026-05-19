# Nhập số nguyên n
n = int(input("Nhập n: "))

# Tính tổng các số từ 1 đến n
tong_day_du = n * (n + 1) // 2

# Tính tổng các số đã nhập
tong_da_nhap = 0
for i in range(n - 1):
    x = int(input(f"Nhập số thứ {i+1}: "))
    tong_da_nhap += x

# Số bị thiếu
so_thieu = tong_day_du - tong_da_nhap

# Xuất kết quả
print("Số bị thiếu trong danh sách là:", so_thieu)
