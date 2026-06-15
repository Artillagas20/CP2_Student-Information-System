import tkinter as tk

root = tk.Tk()
root.title("Student Information System")
root.geometry("700x500")

tk.Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Grade").grid(row=2, column=0, padx=10, pady=10)
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1)

root.mainloop()