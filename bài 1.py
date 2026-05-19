import tkinter as tk
from tkinter import messagebox
import csv
import re
import os

# Tên file lưu trữ
FILE_NAME = "khach_hang.csv"


def validate_data(name, dob, address, phone):
    if not re.match(r"^[a-zA-ZÀ-ỹ\s]+$", name):
        return False, "Tên không được chứa số hoặc ký tự đặc biệt!"

    if not re.match(r"^\d{2}/\d{2}/\d{4}$", dob):

        return False, "Ngày sinh sai định dạng dd/mm/yyyy!"

    if not (phone.isdigit() and len(phone) == 10):
        return False, "Số điện thoại phải gồm 10 chữ số!"

    return True, ""


def save_data():
    name = entry_name.get().strip()
    dob = entry_dob.get().strip()
    address = entry_address.get().strip()
    phone = entry_phone.get().strip()

    is_valid, error_msg = validate_data(name, dob, address, phone)

    if is_valid:
        file_exists = os.path.isfile(FILE_NAME)
        with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([name, dob, address, phone])
        messagebox.showinfo("Thành công", "Đã lưu thông tin khách hàng!")
        clear_entries()
    else:
        messagebox.showerror("Lỗi nhập liệu", error_msg)


def search_data():
    search_terms = {
        'name': entry_name.get().strip(),
        'dob': entry_dob.get().strip(),
        'address': entry_address.get().strip(),
        'phone': entry_phone.get().strip()
    }

    if not any(search_terms.values()):
        messagebox.showwarning("Chú ý", "Hãy nhập ít nhất một trường để tìm kiếm!")
        return

    if not os.path.exists(FILE_NAME):
        messagebox.showerror("Lỗi", "Chưa có dữ liệu khách hàng nào!")
        return

    with open(FILE_NAME, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            match = False
            if (search_terms['name'] and search_terms['name'].lower() in row[0].lower()) or \
                    (search_terms['dob'] == row[1]) or \
                    (search_terms['address'] and search_terms['address'].lower() in row[2].lower()) or \
                    (search_terms['phone'] == row[3]):
                # Hiển thị thông tin tìm thấy lên các ô nhập
                entry_name.delete(0, tk.END);
                entry_name.insert(0, row[0])
                entry_dob.delete(0, tk.END);
                entry_dob.insert(0, row[1])
                entry_address.delete(0, tk.END);
                entry_address.insert(0, row[2])
                entry_phone.delete(0, tk.END);
                entry_phone.insert(0, row[3])
                return

        messagebox.showwarning("Thông báo", "Không tìm thấy khách hàng phù hợp.")


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_phone.delete(0, tk.END)


# --- Thiết lập Giao diện ---
root = tk.Tk()
root.title("Quản lý khách hàng")
root.geometry("400x300")

tk.Label(root, text="Tên:").grid(row=0, column=0, pady=10, padx=10)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Ngày sinh (dd/mm/yyyy):").grid(row=1, column=0, pady=10, padx=10)
entry_dob = tk.Entry(root, width=30)
entry_dob.grid(row=1, column=1)

tk.Label(root, text="Địa chỉ:").grid(row=2, column=0, pady=10, padx=10)
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=2, column=1)

tk.Label(root, text="Số điện thoại:").grid(row=3, column=0, pady=10, padx=10)
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=3, column=1)

btn_save = tk.Button(root, text="Nhập", command=save_data, width=10)
btn_save.grid(row=4, column=0, pady=20)

btn_search = tk.Button(root, text="Tìm", command=search_data, width=10)
btn_search.grid(row=4, column=1, pady=20)

root.mainloop()