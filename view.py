import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controller import StudentController


class StudentView:

    def __init__(self, root):
        self.root = root
        self.controller = StudentController()

        self.selected = None
        self.dark = False

        root.title("Student System")
        root.geometry("900x500")
        root.configure(bg="#ecf0f1")

        # ===== SIDEBAR =====
        self.sidebar = tk.Frame(root, bg="#2c3e50", width=200)
        self.sidebar.pack(side="left", fill="y")

        tk.Label(self.sidebar, text="MENU",
                 bg="#2c3e50", fg="white",
                 font=("Arial", 14, "bold")).pack(pady=20)

        tk.Button(self.sidebar, text="Refresh",
                  bg="#34495e", fg="white",
                  command=self.load).pack(pady=5)

        tk.Button(self.sidebar, text="Clear",
                  bg="#16a085", fg="white",
                  command=self.clear).pack(pady=5)

        tk.Button(self.sidebar, text="Dark Mode",
                  bg="#8e44ad", fg="white",
                  command=self.toggle_dark).pack(pady=5)

        tk.Button(self.sidebar, text="Exit",
                  bg="#e74c3c", fg="white",
                  command=root.destroy).pack(pady=5)

        # ===== MAIN =====
        self.main = tk.Frame(root, bg="#ecf0f1")
        self.main.pack(side="left", fill="both", expand=True)

        tk.Label(self.main, text="STUDENT INFORMATION SYSTEM",
                 font=("Arial", 16, "bold"),
                 bg="#ecf0f1").pack(pady=10)

        # FORM
        form = tk.Frame(self.main, bg="#ecf0f1")
        form.pack()

        tk.Label(form, text="ID", bg="#ecf0f1").grid(row=0, column=0)
        self.id_entry = tk.Entry(form)
        self.id_entry.grid(row=0, column=1)

        tk.Label(form, text="Name", bg="#ecf0f1").grid(row=1, column=0)
        self.name_entry = tk.Entry(form)
        self.name_entry.grid(row=1, column=1)

        tk.Label(form, text="Grade", bg="#ecf0f1").grid(row=2, column=0)
        self.grade_entry = tk.Entry(form)
        self.grade_entry.grid(row=2, column=1)

        # BUTTONS
        btn = tk.Frame(self.main, bg="#ecf0f1")
        btn.pack(pady=10)

        tk.Button(btn, text="Add", bg="green", fg="white",
                  command=self.add).grid(row=0, column=0)

        tk.Button(btn, text="Update", bg="orange", fg="white",
                  command=self.update).grid(row=0, column=1)

        tk.Button(btn, text="Delete", bg="red", fg="white",
                  command=self.delete).grid(row=0, column=2)

        tk.Button(btn, text="Search", bg="blue", fg="white",
                  command=self.search).grid(row=0, column=3)

        # TABLE
        self.table = ttk.Treeview(self.main,
                                  columns=("ID", "Name", "Grade"),
                                  show="headings")

        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Grade", text="Grade")

        self.table.pack(fill="both", expand=True)

        self.table.bind("<ButtonRelease-1>", self.select)

        self.load()

    # ===== LOAD =====
    def load(self):
        for i in self.table.get_children():
            self.table.delete(i)

        for s in self.controller.get_students():
            self.table.insert("", "end",
                               values=(s["id"], s["name"], s["grade"]))

    # ===== SELECT ROW =====
    def select(self, event):
        row = self.table.focus()
        data = self.table.item(row, "values")

        if data:
            self.selected = data[0]
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.grade_entry.delete(0, tk.END)

            self.id_entry.insert(0, data[0])
            self.name_entry.insert(0, data[1])
            self.grade_entry.insert(0, data[2])

    # ===== CLEAR =====
    def clear(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.selected = None

    # ===== ADD =====
    def add(self):
        ok = self.controller.add_student(
            self.id_entry.get(),
            self.name_entry.get(),
            self.grade_entry.get()
        )

        if ok:
            messagebox.showinfo("Success", "Student added!")
            self.load()

    # ===== UPDATE =====
    def update(self):
        if self.selected:
            self.controller.update_student(
                self.id_entry.get(),
                self.name_entry.get(),
                self.grade_entry.get()
            )
            self.load()

    # ===== DELETE =====
    def delete(self):
        if self.selected:
            self.controller.delete_student(self.selected)
            self.load()

    # ===== SEARCH =====
    def search(self):
        s = self.controller.search_student(self.id_entry.get())

        if s:
            for i in self.table.get_children():
                self.table.delete(i)

            self.table.insert("", "end",
                              values=(s["id"], s["name"], s["grade"]))

    # ===== DARK MODE =====
    def toggle_dark(self):
        if not self.dark:
            self.main.configure(bg="#2c3e50")
            self.dark = True
        else:
            self.main.configure(bg="#ecf0f1")
            self.dark = False