import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "http://127.0.0.1:5000/tasks"


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Quản lý Công việc")
        self.root.geometry("650x550")

        # Style trang trí
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Arial", 10), padding=5)
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#d3d3d3")

        # Hàm validate chỉ cho phép nhập số
        vcmd = (self.root.register(self.validate_id_input), '%P')

        # --- Khung nhập liệu ---
        input_frame = tk.LabelFrame(self.root, text=" 📝 Thông tin công việc ", padx=10, pady=10,
                                    font=("Arial", 10, "bold"))
        input_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(input_frame, text="ID:").grid(row=0, column=0, sticky="w", pady=5)
        # Ép nhập số
        self.entry_id = tk.Entry(input_frame, width=15, validate='key', validatecommand=vcmd)
        self.entry_id.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(input_frame, text="Tiêu đề:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_title = tk.Entry(input_frame, width=50)
        self.entry_title.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(input_frame, text="Mô tả:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_desc = tk.Entry(input_frame, width=50)
        self.entry_desc.grid(row=2, column=1, sticky="w", pady=5)

        # Sử dụng Checkbox cho trạng thái
        tk.Label(input_frame, text="Trạng thái:").grid(row=3, column=0, sticky="w", pady=5)
        self.var_done = tk.BooleanVar(value=False)
        self.chk_done = tk.Checkbutton(input_frame, text="Đã hoàn thành", variable=self.var_done)
        self.chk_done.grid(row=3, column=1, sticky="w", pady=5)

        # --- Khung nút bấm Action ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(btn_frame, text="➕ Thêm mới", command=self.add_task, bg="#90ee90", width=12).pack(side="left", padx=5)
        tk.Button(btn_frame, text="💾 Cập nhật", command=self.update_task, bg="#ffd700", width=12).pack(side="left",
                                                                                                       padx=5)
        tk.Button(btn_frame, text="🗑️ Xóa", command=self.delete_task, bg="#ffcccb", width=12).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🧹 Làm mới Form", command=self.clear_form, bg="#e0e0e0", width=12).pack(side="right",
                                                                                                          padx=5)

        # --- Khung Tìm kiếm ---
        search_frame = tk.Frame(self.root)
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame, text="Tìm kiếm (Tiêu đề):").pack(side="left")
        self.entry_search = tk.Entry(search_frame, width=30)
        self.entry_search.pack(side="left", padx=5)
        tk.Button(search_frame, text="🔍 Tìm", command=self.search_tasks, bg="#add8e6").pack(side="left", padx=5)
        tk.Button(search_frame, text="🔄 Tải lại tất cả", command=self.load_tasks).pack(side="left", padx=5)

        # --- Khung hiển thị danh sách ---
        list_frame = tk.LabelFrame(self.root, text=" 📋 Danh sách công việc ", padx=10, pady=10,
                                   font=("Arial", 10, "bold"))
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        columns = ("id", "title", "description", "done")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Tiêu đề")
        self.tree.heading("description", text="Mô tả")
        self.tree.heading("done", text="Hoàn thành?")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("title", width=150)
        self.tree.column("description", width=250)
        self.tree.column("done", width=80, anchor="center")

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.load_tasks()

    # Hàm chỉ cho phép nhập số vào Entry ID
    def validate_id_input(self, value):
        if value.isdigit() or value == "":
            return True
        return False

    def load_tasks(self, search_query=None):
        try:
            url = API_URL
            params = {"title": search_query} if search_query else {}
            response = requests.get(url, params=params, timeout=3)

            if response.status_code == 200:
                self.tree.delete(*self.tree.get_children())
                for task in response.json():
                    status_text = "☑️ Có" if task["done"] else "🔲 Không"
                    self.tree.insert("", tk.END, values=(
                        task["id"], task["title"], task["description"], status_text
                    ))
            else:
                messagebox.showerror("Lỗi", "Không thể tải dữ liệu.")
        except Exception:
            messagebox.showerror("Lỗi", "Không kết nối được API.")

    def search_tasks(self):
        query = self.entry_search.get()
        self.load_tasks(search_query=query)

    def add_task(self):
        title = self.entry_title.get().strip()
        desc = self.entry_desc.get().strip()

        if not title or not desc:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ tiêu đề và mô tả.")
            return

        data = {
            "title": title,
            "description": desc,
            "done": self.var_done.get()
        }

        try:
            response = requests.post(API_URL, json=data, timeout=3)
            if response.status_code == 201:
                messagebox.showinfo("Thành công", "Đã thêm công việc mới.")
                self.load_tasks()
                self.clear_form()
            elif response.status_code == 400:  # Lỗi trùng lặp từ server
                messagebox.showerror("Bỏ qua", response.json().get("error"))
        except Exception:
            messagebox.showerror("Lỗi", "Không kết nối được API.")

    def update_task(self):
        task_id = self.entry_id.get()
        if not task_id:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID hoặc chọn từ danh sách.")
            return

        data = {
            "title": self.entry_title.get().strip(),
            "description": self.entry_desc.get().strip(),
            "done": self.var_done.get()
        }

        try:
            response = requests.put(f"{API_URL}/{task_id}", json=data, timeout=3)
            if response.status_code == 200:
                messagebox.showinfo("Thành công", "Đã cập nhật công việc.")
                self.load_tasks()
            elif response.status_code == 400:  # Lỗi trùng lặp
                messagebox.showwarning("Cảnh báo", response.json().get("error"))
            elif response.status_code == 404:
                messagebox.showerror("Lỗi", "Không tìm thấy ID này.")
        except Exception:
            messagebox.showerror("Lỗi", "Không kết nối được API.")

    def delete_task(self):
        task_id = self.entry_id.get()
        if not task_id:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID hoặc chọn từ danh sách.")
            return

        if not messagebox.askyesno("Xác nhận", f"Xóa công việc ID {task_id}?"):
            return

        try:
            response = requests.delete(f"{API_URL}/{task_id}", timeout=3)
            if response.status_code == 200:
                messagebox.showinfo("Thành công", "Đã xóa công việc.")
                self.load_tasks()
                self.clear_form()
            else:
                messagebox.showerror("Lỗi", response.json().get("error", "Lỗi xóa công việc"))
        except Exception:
            messagebox.showerror("Lỗi", "Không kết nối được API.")

    def on_select(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item)["values"]
            self.clear_form()

            self.entry_id.insert(0, values[0])
            self.entry_title.insert(0, values[1])
            self.entry_description = values[2]

            # Xử lý an toàn khi chèn mô tả
            if isinstance(values[2], str):
                self.entry_desc.insert(0, values[2])

            # Xử lý Checkbox từ giá trị text
            is_done = True if values[3] == "☑️ Có" else False
            self.var_done.set(is_done)

    def clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_title.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)
        self.var_done.set(False)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()